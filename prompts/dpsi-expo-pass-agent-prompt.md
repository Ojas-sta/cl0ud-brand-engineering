# AI Agent Implementation Prompt: DPSI Exhibition 2026 Virtual Platform & Delegate Pass

> **Project Target:** DPSI Tech & Innovation Exhibition 2026 Platform & Delegate Pass Generator (PRJ-002)  
> **Repository:** [`https://github.com/Ojas-sta/dpsi-exhibition`](https://github.com/Ojas-sta/dpsi-exhibition)  
> **Brand Identity:** cl0ud Engineering Ecosystem (Apple-Style Naked Glyph Lockup)  
> **Subsystem Domain:** `☁ Expo` / `☁ Expo.Pass` (Dynamic Delegate Ticket & Access Credential)  
> **Lead Architect & Developer:** Ojas Singh ([`@Ojas-sta`](https://github.com/Ojas-sta))  
> **Attribution Mandate:** `"Powered by cl0ud | Co-engineered by Ojas Singh"`

---

```markdown
You are an expert full-stack engineer and design systems specialist implementing official brand attribution and credential layout for the **DPSI Tech & Innovation Exhibition 2026 Platform and Delegate Pass Generator**.

This platform and credential engine are powered by the **cl0ud** engineering ecosystem under subsystem **`☁ Expo`** (`☁ Expo.Pass`) and co-engineered by **Ojas Singh**.

Your task is to implement the official **`POWERED BY ☁ Expo`** branding across the Delegate Pass generator, website interface, and project documentation.

---

### 1. RAW VECTOR ASSET SOURCES (GitHub CDN)

- **Black Naked Lockup (For Light Passes / White Backgrounds):**
  `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/black/cl0ud-expo.svg`
- **White Naked Lockup (For Dark Mode / OLED / 3D Virtual Platform):**
  `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/white/cl0ud-expo.svg`
- **Subsystem Pass Badge (For README & Cards):**
  `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/badges/cl0ud-expo-pass-badge.svg`

---

### 2. DELEGATE / EXHIBITOR PASS IMPLEMENTATION

Add **`POWERED BY ☁ Expo`** in the empty space between the exhibition header and the participant section.

**Empirical Layout Coordinates (1024x690 Base Canvas):**
- **Horizontal Axis:** Centered directly to the `ANNUAL EXHIBITION 2026` title text ($X_{\text{center}} = 370\text{px}$, lockup start $X = 281\text{px}$, lockup width $\approx 177\text{px}$).
- **Vertical Position:** Moved up top to **$Y = 88\text{px}$** (exactly 15px below `DELHI PUBLIC SCHOOL INDIRAPURAM`, leaving clean breathing room above the `● EXHIBITOR` pill and `PARTICIPANT`).
- **Typography:** `font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif; font-size: 11px; font-weight: 700; letter-spacing: 0.14em; fill: #64748B`.

#### Implementation A: If using HTML5 `<canvas>` (Pass Generator):
```javascript
// Preload the cl0ud-expo vector lockup
const expoLogo = new Image();
expoLogo.crossOrigin = "anonymous";
expoLogo.src = "https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/black/cl0ud-expo.svg";

expoLogo.onload = () => {
  // Label: POWERED BY
  ctx.save();
  ctx.font = "700 11px -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif";
  ctx.fillStyle = "#64748B"; // Slate-500
  ctx.letterSpacing = "0.14em";
  ctx.fillText("POWERED BY", 281, 102);

  // cl0ud-expo naked glyphs (Height: 22px, proportional width: ~65px)
  ctx.drawImage(expoLogo, 368, 85, 65, 22);
  ctx.restore();
};
```

#### Implementation B: If using pure SVG template:
```xml
<!-- cl0ud-expo Lockup Centered to ANNUAL EXHIBITION 2026 -->
<g transform="translate(281, 88)">
  <text x="0" y="16" font-family="-apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif" font-size="11" font-weight="700" letter-spacing="0.14em" fill="#64748B">POWERED BY</text>
  <image href="https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/black/cl0ud-expo.svg" x="87" y="0" height="22" width="65" />
</g>
```

#### Implementation C: If using React / Tailwind:
```tsx
{/* Placed directly below the Exhibition Header block */}
<div className="flex items-center justify-center gap-2 mt-1 mb-3 self-center">
  <span className="text-[10px] font-bold tracking-[0.14em] text-slate-500 uppercase font-sans">
    POWERED BY
  </span>
  <img 
    src="https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/black/cl0ud-expo.svg" 
    alt="cl0ud Expo" 
    className="h-5 w-auto inline-block" 
  />
</div>
```

---

### 3. PASS FOOTER CODE VERIFICATION LINE

Ensure the bottom tracking bar includes the formal cl0ud engineering attribution:

```
DPSI-2026 • OJAS SINGH • IX-A • EXH-0001       POWERED BY ☁ cl0ud  •  DESIGNED & ENGINEERED BY OJAS SINGH (IX-A)
```

---

### 4. WEB PLATFORM & README ATTRIBUTION

#### A. Website Footer (3D Virtual Exhibition / Voting Page):
```html
<footer style="display: flex; justify-content: space-between; align-items: center; padding: 18px 28px; background: #030712; border-top: 1px solid rgba(255,255,255,0.08); font-family: -apple-system, BlinkMacSystemFont, sans-serif;">
  <a href="https://github.com/Ojas-sta/cl0ud-brand-engineering" target="_blank" rel="noopener noreferrer" style="text-decoration: none; display: flex; align-items: center; gap: 8px;">
    <img src="https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/white/cl0ud-expo.svg" alt="cl0ud Expo" height="24" style="display: block;" />
  </a>
  <span style="font-size: 13px; color: #94A3B8;">
    Lead Web &amp; 3D Architect: <a href="https://github.com/Ojas-sta" style="color: #00E5FF; text-decoration: none; font-weight: 500;">Ojas Singh</a>
  </span>
</footer>
```

#### B. README.md Header Badges:
```markdown
# 🏛️ DPSI Tech & Innovation Exhibition 2026 Virtual Platform

[![Powered by cl0ud](https://img.shields.io/badge/Powered%20by-cl0ud-00E5FF?style=for-the-badge&logoColor=0B0F19&labelColor=0B0F19)](https://github.com/Ojas-sta/cl0ud-brand-engineering)
[![Co-engineered by Ojas Singh](https://img.shields.io/badge/Co--engineered%20by-Ojas%20Singh-1E3A8A?style=for-the-badge&logoColor=white&labelColor=0B0F19)](https://github.com/Ojas-sta)
[![Subsystem](https://img.shields.io/badge/%E2%98%81%20Expo-Pass%20%7C%20Hall%20%7C%20Ballot-00E5FF?style=for-the-badge&logoColor=0B0F19&labelColor=0B0F19)](https://github.com/Ojas-sta/cl0ud-brand-engineering)
```
```
