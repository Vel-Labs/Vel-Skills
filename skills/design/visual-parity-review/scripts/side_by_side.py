#!/usr/bin/env python3
"""Compose a reference image and one or more build captures side by side.

Usage:
    python3 side_by_side.py OUT.png REFERENCE.png BUILD.png [BUILD2.png ...]
        [--crop HEIGHT] [--scale 0.5] [--labels "Reference,Build dark,Build light"]

Each image is cropped to HEIGHT (if given), scaled, and placed left to right with a
label strip on top, so a reviewer compares the same region at the same size.
Requires Pillow.
"""

import argparse

from PIL import Image, ImageDraw


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("out")
    parser.add_argument("images", nargs="+")
    parser.add_argument("--crop", type=int, default=None)
    parser.add_argument("--scale", type=float, default=0.5)
    parser.add_argument("--labels", default="")
    args = parser.parse_args()

    labels = [s.strip() for s in args.labels.split(",")] if args.labels else []
    images = []
    for path in args.images:
        image = Image.open(path).convert("RGB")
        if args.crop:
            image = image.crop((0, 0, image.width, min(image.height, args.crop)))
        size = (int(image.width * args.scale), int(image.height * args.scale))
        images.append(image.resize(size))

    gap, strip = 12, 28
    width = sum(i.width for i in images) + gap * (len(images) - 1)
    height = max(i.height for i in images) + strip
    canvas = Image.new("RGB", (width, height), (128, 128, 128))
    draw = ImageDraw.Draw(canvas)
    x = 0
    for index, image in enumerate(images):
        canvas.paste(image, (x, strip))
        name = labels[index] if index < len(labels) else args.images[index]
        draw.text((x + 6, 8), name, fill=(255, 255, 255))
        x += image.width + gap
    canvas.save(args.out)
    print(args.out)


if __name__ == "__main__":
    main()
