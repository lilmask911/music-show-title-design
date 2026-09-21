# Typography Direction Library

Choose directions that fit the reference and user request. For a six-version batch, use six meaningfully different rows rather than minor variations.

| Direction | Chinese main title | English layer | Depth/composition |
|---|---|---|---|
| Semi-cursive signature | expressive semi-cursive brush, varied pressure | oversized loose fashion script | red ghost sweep behind, centered micro-credit |
| Song × Didone | formal high-contrast Song/Ming | narrow italic Didone serif | cropped back layer, fine outline echo, precise baseline |
| Modern heavy poster | compact geometric Chinese black type | ultra-condensed sans | broad architectural band, offset extrusion |
| Clerical-stele hybrid | broad horizontals and restrained flared endings | thin monoline signature | loops through negative space, small block accent |
| Vertical editorial | stacked formal Chinese | rotated or vertical Latin serif | vertical rule, asymmetric grid, tiny horizontal credit |
| Rugged dry brush | broken bristle texture, decisive angular strokes | engraved serif italic | darker outline duplicate and short rules |
| Deconstructed slice | legible title split into offset slices | small formal serif | shifted bands, restrained echo, strict baseline |
| Quiet minimal | clean semi-cursive or fine Song | one oversized faint script | extreme scale contrast and generous negative space |

## Layer Hierarchy

Use four levels when the user asks for stronger depth:

1. Foreground: exact Chinese title, highest contrast and sharpest edges.
2. Midground: English title crossing behind or through negative space.
3. Background: one blurred, outlined, or offset echo at lower contrast.
4. Tertiary: artist/credit line and at most two short rules or one small block.

Do not add filler copy to simulate editorial detail. Information density comes from scale, overlap, tracking, and repetition of the approved title—not invented words.

## Prompt Skeleton

```text
Use case: logo-brand
Asset type: transparent 16:9 title overlay for a Chinese music show / cinematic MV
Input image: style and composition reference only
Exact readable text only: "<中文标题>", "<英文标题>", "<署名>"
Typography: <chosen direction>
Layering: crisp foreground Chinese; overlapping English middle layer; one restrained background echo; tertiary credit
Palette: <user palette or restrained reference-derived accent>
Background: genuine transparent RGBA, no checkerboard pattern
Constraints: no other text, people, scenery, UI, logo, emblem, watermark, frame, or mockup
```

For a black-background fallback, replace the background line with: “perfectly uniform solid pure black #000000 intended only for later alpha extraction; no texture, vignette, or checkerboard.”

