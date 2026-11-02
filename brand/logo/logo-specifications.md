# cl0ud — Logo Specifications & Vector Construction

> **System Designation:** Logo Construction & Vector Standards  
> **Primary Vector Asset:** [`assets/logos/cl0ud-primary.svg`](file:///Users/roopalisingh/Desktop/cl0ud/assets/logos/cl0ud-primary.svg)  
> **Brand Mark:** cl0ud  
> **Specification Reference:** [`cl0ud-brand-spec.json`](file:///Users/roopalisingh/Desktop/cl0ud/cl0ud-brand-spec.json)

---

## 1. Vector Geometry & Construction

The cl0ud primary mark is built upon a precision geometric grid. It combines:
1. **The Cloud Topology Outline:** Three contiguous circular arcs tangent to an open base line, anchored with $1.5\text{px}$ hardware telemetry nodes.
2. **The Discrete Binary Core (`0`):** An optical ellipse ($r_x = 4.5\text{px}, r_y = 6.0\text{px}$) bisected by an internal $45^\circ$ diagonal spark line, representing computation and ground potential.
3. **The Precision Wordmark:** Rendered with `Outfit` (700 Bold) for `cl` and `ud`, with the central `0` set in `JetBrains Mono` (800 Extra-Bold) in Electric Cyan (`#00E5FF`).

```
           ╭──────╮
       ╭──╯        ╰──╮
     ╭─╯     (0)      ╰─╮
     ╰─●──────────────●─╯
```

---

## 2. Technical SVG Specifications

- **ViewBox:** `0 0 280 70` (Primary Lockup) | `0 0 64 64` (Standalone Icon)
- **Stroke Width:** Standard $2.5\text{px}$ vector line with round line-caps (`stroke-linecap="round"`) and round joins (`stroke-linejoin="round"`).
- **Coordinate Precision:** Normalized to 2 decimal places to minimize file size while eliminating subpixel rendering jitter.
- **Responsiveness:** Scalable vector container with `fill="none"` and viewBox preservation.

---

## 3. Clear Space Rules

```
     ┌───────────────────────────────────────────────────┐
     │                     ↑ 1.0X                        │
     │      ← 1.0X →   [ cl0ud MARK ]   ← 1.0X →         │
     │                     ↓ 1.0X                        │
     └───────────────────────────────────────────────────┘
```

The clearance unit **$X$** is defined as the height of the letter **`c`** in the wordmark:
- At standard $70\text{px}$ container height: $X \approx 20\text{px}$.
- The exclusion zone on all four sides must measure at least **$24\text{px}$** in digital layouts.

---

## 4. Minimum Sizes & Export Settings

### Sizing Limits
- **Screen Display:** Minimum width of primary lockup is $140\text{px}$ ($35\text{px}$ height). For smaller spaces, switch to `assets/logos/cl0ud-icon.svg`.
- **Favicon Display:** Minimum size $16\text{px} \times 16\text{px}$ using [`assets/icons/favicon.svg`](file:///Users/roopalisingh/Desktop/cl0ud/assets/icons/favicon.svg).
- **Print / Laser Engraving:** Minimum height of standalone icon is $8\text{mm}$.

### Export Profiles
- **Vector:** SVG 1.1 compliant, paths converted to outlines when exporting to EPS or DXF for laser cutting.
- **Raster:** Lossless PNG with 8-bit alpha channel, rendered at 1x, 2x (@2x Retina), and 4x (@4x Print Master).
- **Color Profile:** sRGB for web and displays; ISO Coated v2 (ECI) for industrial print collateral.
