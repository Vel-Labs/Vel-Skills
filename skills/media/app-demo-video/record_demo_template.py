#!/usr/bin/env python3
"""Scripted Playwright screen recording of a real web app session.

Edit ACTIONS to match the product. Do not inject in-page caption overlays;
captions are composited later by edit_demo.py so they never cover the UI.

The app server must already be running at BASE.

  python record_demo_template.py --out /tmp/demo_raw.webm
  python record_demo_template.py --out /tmp/demo_raw.mp4 --transcode
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

# --- parameters (override with flags) ---------------------------------------
BASE = "http://127.0.0.1:8765"
VIEWPORT = {"width": 1920, "height": 900}  # 16:10 app pane; 180px bar is added in edit
# Optional system Chrome. If the file is missing, Playwright's installed Chromium is used.
CHROME = "/usr/bin/google-chrome"
# ---------------------------------------------------------------------------


def actions(page) -> None:
    """Drive one continuous take. Replace the body with the product's flow.

    Guidelines:
    - Wait for a visible selector before clicking.
    - Hold 2-4 seconds after each state change so the beat is readable.
    - Scroll slower than a person would (wheel + short sleeps).
    - Upload real data; do not mock the on-screen numbers.
    - If you replay a previously recorded run, the later captions should say so.
    """
    page.goto(BASE)
    page.wait_for_selector("text=Drop a data CSV here")
    time.sleep(3)

    # Example beats — delete and rewrite:
    # page.hover("text=Download CSV template")
    # time.sleep(1)
    # with page.expect_download() as dl:
    #     page.click("text=Download CSV template")
    # time.sleep(2)
    # page.set_input_files("input[type=file]", str(Path("data.csv").resolve()))
    # page.wait_for_selector("text=Validated")
    # time.sleep(3)
    # page.click("text=Ignite")  # or start a replay fixture
    # page.wait_for_selector("text=Mission complete", timeout=120_000)
    # time.sleep(4)
    # for _ in range(24):
    #     page.mouse.wheel(0, 140)
    #     time.sleep(0.6)
    # page.evaluate("window.scrollTo({top: 0, behavior: 'smooth'})")
    # time.sleep(3)

    time.sleep(2)


def transcode_h264(src: Path, dst: Path, fps: int | None) -> None:
    cmd = [
        "ffmpeg", "-y", "-v", "error", "-i", str(src),
        "-c:v", "libx264", "-preset", "slow", "-crf", "22",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart",
    ]
    if fps:
        cmd += ["-r", str(fps)]
    cmd.append(str(dst))
    subprocess.run(cmd, check=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", default=BASE)
    ap.add_argument("--out", required=True, help="Output .webm (raw) or .mp4 (with --transcode)")
    ap.add_argument("--width", type=int, default=VIEWPORT["width"])
    ap.add_argument("--height", type=int, default=VIEWPORT["height"])
    ap.add_argument("--chrome", default=CHROME)
    ap.add_argument("--transcode", action="store_true",
                    help="Also write H.264 mp4 (keeps source fps unless --fps is set)")
    ap.add_argument("--fps", type=int, default=0,
                    help="Only used with --transcode. 0 = keep Playwright's native rate.")
    args = ap.parse_args()

    out = Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    vp = {"width": args.width, "height": args.height}
    tmp = out.parent / f".{out.stem}_rec"
    tmp.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        chrome_path = args.chrome if Path(args.chrome).is_file() else None
        launch_kw = {"args": ["--no-sandbox"]}
        if chrome_path:
            launch_kw["executable_path"] = chrome_path
        browser = p.chromium.launch(**launch_kw)
        ctx = browser.new_context(
            viewport=vp,
            record_video_dir=str(tmp),
            record_video_size=vp,
            accept_downloads=True,
        )
        page = ctx.new_page()
        t0 = time.monotonic()
        actions(page)
        dur = time.monotonic() - t0
        video = page.video
        ctx.close()
        browser.close()
        src = Path(video.path())

    raw = out if out.suffix.lower() == ".webm" and not args.transcode else tmp / "raw.webm"
    if src != raw:
        src.replace(raw)
    if args.transcode or out.suffix.lower() == ".mp4":
        dest = out if out.suffix.lower() == ".mp4" else out.with_suffix(".mp4")
        transcode_h264(raw, dest, args.fps or None)
        print(f"recorded {dur:.1f}s -> {dest}")
        if dest != raw and raw.exists() and out.suffix.lower() != ".webm":
            raw.unlink(missing_ok=True)
    else:
        if raw != out:
            raw.replace(out)
        print(f"recorded {dur:.1f}s -> {out}")

    for leftover in tmp.glob("*"):
        leftover.unlink()
    if tmp.exists():
        tmp.rmdir()
    return 0


if __name__ == "__main__":
    sys.exit(main())
