#!/usr/bin/env python3
"""Convert bright title artwork on a uniform black canvas to true RGBA.

If the input already contains useful alpha, it is preserved. Optional black
contact and ambient shadows are composited beneath the face layer so white
titles remain dimensional over light video frames.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--threshold", type=float, default=4.0)
    parser.add_argument("--accent-peak", type=float, default=210.0)
    parser.add_argument("--contact-opacity", type=float, default=0.48)
    parser.add_argument("--ambient-opacity", type=float, default=0.26)
    parser.add_argument("--no-shadow", action="store_true")
    return parser.parse_args()


def extract_face(image: Image.Image, threshold: float, accent_peak: float) -> Image.Image:
    if image.mode == "RGBA" and image.getchannel("A").getextrema()[0] == 0:
        return image.copy()

    rgb = np.asarray(image.convert("RGB"), dtype=np.float32)
    hi = rgb.max(axis=2)
    lo = rgb.min(axis=2)
    saturation = (hi - lo) / np.maximum(hi, 1.0)

    white_alpha = hi / 255.0
    accent_alpha = hi / max(accent_peak, 1.0)
    alpha = np.where(saturation > 0.16, accent_alpha, white_alpha)
    alpha = np.where(hi <= threshold, 0.0, alpha)
    alpha = np.clip(alpha, 0.0, 1.0)

    safe = np.maximum(alpha, 1.0 / 255.0)
    face_rgb = np.clip(rgb / safe[..., None], 0, 255)
    face_rgb[alpha <= 0] = 0
    rgba = np.dstack((face_rgb, alpha * 255.0)).astype(np.uint8)
    return Image.fromarray(rgba, "RGBA")


def shifted(mask: Image.Image, dx: int, dy: int) -> Image.Image:
    out = Image.new("L", mask.size, 0)
    out.paste(mask, (dx, dy))
    return out


def shadow_layer(mask: Image.Image, blur: float, dx: int, dy: int, opacity: float) -> Image.Image:
    alpha = shifted(mask.filter(ImageFilter.GaussianBlur(blur)), dx, dy)
    alpha = alpha.point(lambda value: round(value * max(0.0, min(opacity, 1.0))))
    layer = Image.new("RGBA", mask.size, (0, 0, 0, 0))
    layer.putalpha(alpha)
    return layer


def main() -> None:
    args = parse_args()
    source = Image.open(args.input)
    face = extract_face(source, args.threshold, args.accent_peak)

    final = Image.new("RGBA", face.size, (0, 0, 0, 0))
    if not args.no_shadow:
        mask = face.getchannel("A")
        final.alpha_composite(shadow_layer(mask, 16, 13, 17, args.ambient_opacity))
        final.alpha_composite(shadow_layer(mask, 4, 5, 7, args.contact_opacity))
    final.alpha_composite(face)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    final.save(args.output, optimize=True)

    alpha_range = final.getchannel("A").getextrema()
    if alpha_range[0] != 0:
        raise SystemExit("Output has no transparent pixels")
    print(f"saved={args.output}")
    print(f"mode={final.mode} alpha={alpha_range} size={final.size}")


if __name__ == "__main__":
    main()
