# cl0ud — Logo Specifications & Vector Construction

> **System Designation:** Logo Construction & Vector Standards  
> **Primary Vector Asset:** [`assets/logos/cl0ud-primary.svg`](file:///Users/roopalisingh/Desktop/cl0ud/assets/logos/cl0ud-primary.svg)  
> **Brand Mark:** cl0ud  
> **Specification Reference:** [`cl0ud-brand-spec.json`](file:///Users/roopalisingh/Desktop/cl0ud/cl0ud-brand-spec.json)

---

## 1. Vector Geometry & Construction

The official cl0ud mark features the distinctive **Infinity-Cloud Topology**—an interlocking continuous monoline ribbon that forms a cloud silhouette intertwined with an infinity loop ($\infty$), symbolizing computational continuity, ground loops, and hardware integration.

```
            ╭───────────────╮
         ╭──╯   ╭──────╮    ╰──╮
       ╭─╯     │  ╭───╮ │      ╰─╮
       │   ╭───╯  │   │ ╰───╮    │
       ╰───┴──────┴───┴─────┴────╯
```

### Key Geometric Elements:
1. **The Interlocking Ribbon Stroke:** A uniform, bold stroke that ascends on the left, loops smoothly across the upper canopy, sweeps downward in a reverse S-curve into the internal core, and anchors horizontally along the base.
2. **Master Vector Source:** Vectorized and normalized directly from the official master artwork ([`assets/logos/cl0ud-icon.svg`](file:///Users/roopalisingh/Desktop/cl0ud/assets/logos/cl0ud-icon.svg) and reference image [`assets/reference/cl0ud-official-logo-master.jpg`](file:///Users/roopalisingh/Desktop/cl0ud/assets/reference/cl0ud-official-logo-master.jpg)).
3. **Aspect Ratio:** $608\text{px} \times 408\text{px}$ ($\approx 1.49 : 1$, or $3:2$).

---

## 2. Official Credit Card Component & Plaque Spec

The official engineering attribution credit card ([`assets/badges/cl0ud-credit-card.svg`](file:///Users/roopalisingh/Desktop/cl0ud/assets/badges/cl0ud-credit-card.svg) and reference [`assets/reference/cl0ud-credit-card-spec.png`](file:///Users/roopalisingh/Desktop/cl0ud/assets/reference/cl0ud-credit-card-spec.png)) defines the standardized physical and digital attribution card:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        POWERED BY cl0ud ☁️                              │
├────────────────────────────────────────────────────────────────────────┤
│                            CO-ENGINEERED BY                            │
│                               OJAS SINGH                               │
│                 Engineering • Innovation • Development                 │
└────────────────────────────────────────────────────────────────────────┘
```

- **Container:** Rounded rectangle ($R=22\text{px}$), pitch black background (`#000000`), subtle border (`#262626`).
- **Top Row:** `POWERED BY cl0ud` paired with the cyan outline infinity-cloud icon (`#38BDF8`).
- **Divider:** 1px hairline divider (`#262626`).
- **Role Line:** `CO-ENGINEERED BY` in muted slate (`#A1A1AA`), $15\text{px}$, letter-spacing $0.14\text{em}$.
- **Name Line:** `OJAS SINGH` in bright white (`#FFFFFF`), $26\text{px}$, bold.
- **Discipline Tagline:** `Engineering • Innovation • Development` in muted slate (`#A1A1AA`), $14\text{px}$.

---

## 3. Technical SVG Specifications

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
