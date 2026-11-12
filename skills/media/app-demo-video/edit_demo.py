#!/usr/bin/env python3
"""Composite a reserved-caption-bar app demo: title card, punch-ins, end card.

Reads a timeline JSON (see example_timeline.json) and a raw screen recording
whose picture is the app only (typically 1920x900 or 1440x900). The output is
1920x1080: a 1920x900 app pane over a 180px caption bar. Punch-ins zoom the
app pane only. Cuts are hard cuts. A silent AAC track is muxed in.

  python edit_demo.py --input recording.mp4 --timeline example_timeline.json --output demo.mp4
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
APP_H = 900
BAR_H = H - APP_H  # 180
GOLD_Y = 0  # gold rule is the first rows of the bar
GOLD = (225, 160, 29)       # #E1A01D
BG = (8, 7, 12)             # #08070C
CREAM = (243, 236, 227)     # #F3ECE3
SUB = (154, 149, 140)       # #9A958C
GOLD_RULE_PX = 4

def _first_font(candidates):
    for c in candidates:
        if not c:
            continue
        p = Path(c).expanduser()
        if p.is_file():
            return p
    return None


def _resolve_fonts():
    """Prefer APP_DEMO_FONT / APP_DEMO_FONT_ITALIC, then ./fonts, then common system faces.

    Caption headlines look best in a heavy italic grotesk (Geist Italic 900 is a
    good stand-in). Drop .ttf files into ./fonts if you have a preferred family.
    """
    here = Path(__file__).resolve().parent
    italic = _first_font([
        os.environ.get("APP_DEMO_FONT_ITALIC"),
        here / "fonts" / "Geist-Italic.ttf",
        here / "fonts" / "Italic.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf",
        "/Library/Fonts/Arial Italic.ttf",
    ])
    regular = _first_font([
        os.environ.get("APP_DEMO_FONT"),
        here / "fonts" / "Geist.ttf",
        here / "fonts" / "Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/Library/Fonts/Arial.ttf",
    ])
    if not italic or not regular:
        raise SystemExit(
            "No usable font found. Install a .ttf (Geist, Inter, or similar) under ./fonts/ "
            "or set APP_DEMO_FONT and APP_DEMO_FONT_ITALIC to font files."
        )
    return regular, italic


GEIST, GEIST_ITALIC = _resolve_fonts()


def font(path: Path, size: int, weight: int = 400) -> ImageFont.FreeTypeFont:
    f = ImageFont.truetype(str(path), size=size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f


def _text_size(draw: ImageDraw.ImageDraw, text: str, fnt) -> tuple[int, int]:
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[2] - b[0], b[3] - b[1]


def wrap_lines(draw, text: str, fnt, max_width: int) -> list[str]:
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if _text_size(draw, trial, fnt)[0] <= max_width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [""]


def kicker_width(text: str, fnt, tracking: int = 5) -> int:
    dummy = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    w = 0
    for i, ch in enumerate(text):
        w += _text_size(dummy, ch, fnt)[0]
        if i < len(text) - 1:
            w += tracking
    return w


def draw_kicker(draw, x, y, text, fnt, fill, tracking: int = 5) -> None:
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += _text_size(draw, ch, fnt)[0] + tracking


def draw_bar(img: Image.Image, kicker: str, caption: str) -> None:
    """Paint the 180px reserved bar at the bottom of a 1920x1080 canvas."""
    d = ImageDraw.Draw(img)
    top = APP_H
    d.rectangle((0, top, W, H), fill=BG)
    d.rectangle((0, top, W, top + GOLD_RULE_PX), fill=GOLD)
    kicker_font = font(GEIST, 22, 500)
    cap_font = font(GEIST_ITALIC, 52, 900)
    draw_kicker(d, 48, top + 18, kicker.upper(), kicker_font, GOLD, tracking=5)
    lines = wrap_lines(d, caption, cap_font, W - 96)
    y = top + 52
    for line in lines[:2]:
        d.text((48, y), line, font=cap_font, fill=CREAM)
        y += 58


def render_title_card(spec: dict, dest: Path) -> None:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    kicker_font = font(GEIST, 22, 500)
    head_font = font(GEIST_ITALIC, 92, 900)
    sub_font = font(GEIST, 32, 400)
    kicker = spec.get("kicker") or ""
    lines = spec.get("lines") or [spec.get("title") or ""]
    sub = spec.get("sub") or ""
    # vertical stack, roughly centered in the app pane
    heads = lines if isinstance(lines, list) else [str(lines)]
    rendered = []
    total_h = 0
    for line in heads:
        wh = _text_size(d, line, head_font)
        rendered.append((line, wh))
        total_h += wh[1] + 8
    sub_h = _text_size(d, sub, sub_font)[1] if sub else 0
    block = 28 + total_h + (24 + sub_h if sub else 0)
    y = (APP_H - block) // 2
    kw = kicker_width(kicker.upper(), kicker_font, tracking=6)
    draw_kicker(d, (W - kw) // 2, y, kicker.upper(), kicker_font, GOLD, tracking=6)
    y += 44
    for line, (lw, lh) in rendered:
        d.text(((W - lw) // 2, y), line, font=head_font, fill=CREAM)
        y += lh + 8
    if sub:
        y += 20
        sw = _text_size(d, sub, sub_font)[0]
        d.text(((W - sw) // 2, y), sub, font=sub_font, fill=SUB)
    draw_bar(img, spec.get("caption_kicker") or kicker, spec.get("caption") or " ".join(heads))
    img.save(dest)


def render_end_card(spec: dict, dest: Path) -> None:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    kicker_font = font(GEIST, 22, 500)
    head_font = font(GEIST_ITALIC, 40, 800)
    body_font = font(GEIST, 28, 400)
    kicker = spec.get("kicker") or "THE CATCH"
    # rounded rectangle in the app pane
    box = (160, 220, W - 160, APP_H - 80)
    d.rounded_rectangle(box, radius=18, outline=GOLD, width=2)
    inner_bg = (14, 12, 8)
    d.rounded_rectangle((box[0] + 2, box[1] + 2, box[2] - 2, box[3] - 2), radius=16, fill=inner_bg)
    kw = kicker_width(kicker.upper(), kicker_font, tracking=6)
    draw_kicker(d, (W - kw) // 2, box[1] - 36, kicker.upper(), kicker_font, GOLD, tracking=6)
    y = box[1] + 48
    x = box[0] + 48
    max_w = box[2] - box[0] - 96
    # body is a list of {title, text} or a list of strings
    for block in spec.get("body") or []:
        if isinstance(block, dict):
            title = block.get("title") or ""
            text = block.get("text") or ""
            line = f"{title} {text}".strip()
            # paint title in gold, rest in cream — split if title is a prefix
            if title and text:
                tw, th = _text_size(d, title, head_font)
                d.text((x, y), title, font=head_font, fill=GOLD)
                rest_lines = wrap_lines(d, text, body_font, max_w)
                # first wrapped line of body under or beside? keep body below title
                y += th + 8
                for rl in rest_lines:
                    d.text((x, y), rl, font=body_font, fill=CREAM)
                    y += 36
                y += 28
            else:
                for rl in wrap_lines(d, line, body_font, max_w):
                    d.text((x, y), rl, font=body_font, fill=CREAM)
                    y += 36
                y += 16
        else:
            for rl in wrap_lines(d, str(block), body_font, max_w):
                d.text((x, y), rl, font=body_font, fill=CREAM)
                y += 36
            y += 16
    draw_bar(img, spec.get("caption_kicker") or kicker, spec.get("caption") or "")
    img.save(dest)


def render_bar_png(kicker: str, caption: str, dest: Path) -> None:
    img = Image.new("RGB", (W, BAR_H), BG)
    # draw_bar expects a full canvas; paste into one
    full = Image.new("RGB", (W, H), BG)
    draw_bar(full, kicker, caption)
    full.crop((0, APP_H, W, H)).save(dest)


def ff(*args: str) -> None:
    subprocess.run(["ffmpeg", "-y", "-v", "error", *args], check=True)


def ffprobe_duration(path: Path) -> float:
    out = subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(path),
    ], text=True).strip()
    return float(out)


def fit_app_filter(src_w: int, src_h: int, zoom: dict | None, duration: float, fps: int) -> str:
    """Scale/pad the source into 1920x900, optionally punch-in mid-clip.

    zoom = {at, scale, cx, cy, duration} where at/duration are seconds into this
    beat, cx/cy are 0-1 relative centers, scale is the hold zoom (e.g. 1.3).
    """
    # First fit source into 1920x900 (pad with the same near-black).
    # Then, if zoom is set, animate a crop from 1x to `scale` over zoom.duration
    # starting at zoom.at, and hold.
    base = (
        f"scale={W}:{APP_H}:force_original_aspect_ratio=decrease,"
        f"pad={W}:{APP_H}:(ow-iw)/2:(oh-ih)/2:color=0x08070C,setsar=1"
    )
    if not zoom:
        return base
    scale = float(zoom.get("scale") or 1.3)
    at = float(zoom.get("at") or 0)
    zdur = max(0.04, float(zoom.get("duration") or 0.4))
    cx = float(zoom.get("cx") if zoom.get("cx") is not None else 0.5)
    cy = float(zoom.get("cy") if zoom.get("cy") is not None else 0.45)
    # zoompan uses a 1-based on-the-fly zoom. Work in the already-fitted 1920x900
    # canvas. z(t) eases from 1 to `scale` between at and at+zdur, then holds.
    # zoompan output size must be set; fps must match.
    # Input to zoompan is the padded 1920x900 stream.
    # p= zoom center in pixels of the input.
    zexpr = (
        f"if(lt(in_time\\,{at})\\,1\\,"
        f"if(lt(in_time\\,{at + zdur})\\,1+({scale}-1)*(in_time-{at})/{zdur}\\,{scale}))"
    )
    # x/y keep the focus point centered as zoom grows
    xexpr = f"({cx}*iw)-((({cx}*iw)/zoom))"
    # zoompan's x is the left of the crop window. We want the point cx*iw to stay
    # at cx of the output: x = cx*iw - cx*(iw/zoom) = cx*iw*(1-1/zoom)
    xexpr = f"{cx}*iw*(1-1/zoom)"
    yexpr = f"{cy}*ih*(1-1/zoom)"
    # zoompan can drift; d= frames to emit. We'll just apply it for the whole clip.
    frames = max(1, int(round(duration * fps)))
    return (
        f"{base},zoompan=z='{zexpr}':x='{xexpr}':y='{yexpr}':"
        f"d=1:s={W}x{APP_H}:fps={fps},trim=duration={duration:.4f},setpts=PTS-STARTPTS"
    )


def probe_wh(path: Path) -> tuple[int, int]:
    out = subprocess.check_output([
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height", "-of", "csv=p=0", str(path),
    ], text=True).strip()
    w, h = out.split(",")[0:2]
    return int(w), int(h)


def still_to_clip(png: Path, seconds: float, fps: int, dest: Path) -> None:
    ff(
        "-loop", "1", "-framerate", str(fps), "-i", str(png),
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
        "-t", f"{seconds:.3f}",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "8k",
        "-r", str(fps), str(dest),
    )


def compose_beat(src: Path, beat: dict, fps: int, dest: Path, tmp: Path, idx: int) -> None:
    start = float(beat["start"])
    end = float(beat["end"])
    dur = end - start
    if dur <= 0:
        raise SystemExit(f"beat {idx}: end must be after start")
    bar_png = tmp / f"bar_{idx:02d}.png"
    render_bar_png(beat.get("kicker") or "", beat.get("caption") or "", bar_png)
    app_mp4 = tmp / f"app_{idx:02d}.mp4"
    vf = fit_app_filter(*probe_wh(src), beat.get("zoom"), dur, fps)
    ff(
        "-ss", f"{start:.3f}", "-t", f"{dur:.3f}", "-i", str(src),
        "-vf", vf,
        "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
        "-pix_fmt", "yuv420p", "-r", str(fps), str(app_mp4),
    )
    # vstack app + bar, add silence
    ff(
        "-i", str(app_mp4), "-i", str(bar_png),
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
        "-filter_complex", f"[0:v][1:v]vstack=inputs=2,format=yuv420p,trim=duration={dur:.4f}[v]",
        "-map", "[v]", "-map", "2:a", "-t", f"{dur:.3f}",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
        "-c:a", "aac", "-b:a", "8k", "-r", str(fps), str(dest),
    )


def concat_and_finish(parts: list[Path], fps: int, dest: Path, tmp: Path) -> None:
    lst = tmp / "concat.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in parts), encoding="utf-8")
    ff(
        "-f", "concat", "-safe", "0", "-i", str(lst),
        "-c:v", "libx264", "-preset", "slow", "-crf", "22",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "8k",
        "-movflags", "+faststart", "-r", str(fps), str(dest),
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True, help="Raw screen recording (app only)")
    ap.add_argument("--timeline", required=True, help="JSON beat list")
    ap.add_argument("--output", required=True)
    ap.add_argument("--fps", type=int, default=0, help="0 = use the source frame rate (rounded)")
    args = ap.parse_args()

    src = Path(args.input).resolve()
    tl = json.loads(Path(args.timeline).read_text(encoding="utf-8"))
    dest = Path(args.output).resolve()
    dest.parent.mkdir(parents=True, exist_ok=True)

    if not src.exists():
        raise SystemExit(f"missing input: {src}")
    src_dur = ffprobe_duration(src)
    if not args.fps:
        # keep source rate
        rate = subprocess.check_output([
            "ffprobe", "-v", "error", "-select_streams", "v:0",
            "-show_entries", "stream=r_frame_rate", "-of", "default=nw=1:nk=1", str(src),
        ], text=True).strip()
        if "/" in rate:
            a, b = rate.split("/", 1)
            fps = int(round(int(a) / int(b))) if int(b) else 25
        else:
            fps = int(round(float(rate)))
    else:
        fps = args.fps
    if fps <= 0:
        fps = 25

    tmp = Path(tempfile.mkdtemp(prefix="edit_demo_"))
    parts: list[Path] = []
    try:
        if tl.get("title"):
            png = tmp / "title.png"
            render_title_card(tl["title"], png)
            clip = tmp / "title.mp4"
            still_to_clip(png, float(tl["title"].get("seconds") or 2), fps, clip)
            parts.append(clip)

        for i, beat in enumerate(tl.get("clips") or []):
            if float(beat["end"]) > src_dur + 0.05:
                print(f"warning: beat {i} end {beat['end']} past source duration {src_dur:.2f}s; clamping",
                      file=sys.stderr)
                beat = dict(beat)
                beat["end"] = min(float(beat["end"]), src_dur)
                if beat["end"] - float(beat["start"]) <= 0.05:
                    print(f"warning: skipping beat {i}, no duration left", file=sys.stderr)
                    continue
            clip = tmp / f"beat_{i:02d}.mp4"
            compose_beat(src, beat, fps, clip, tmp, i)
            parts.append(clip)

        if tl.get("end"):
            png = tmp / "end.png"
            render_end_card(tl["end"], png)
            clip = tmp / "end.mp4"
            still_to_clip(png, float(tl["end"].get("seconds") or 3), fps, clip)
            parts.append(clip)

        if not parts:
            raise SystemExit("timeline has no title, clips, or end card")
        concat_and_finish(parts, fps, dest, tmp)
        print(f"wrote {dest} ({ffprobe_duration(dest):.2f}s, {fps} fps)")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
