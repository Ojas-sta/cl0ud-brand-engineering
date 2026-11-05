# AI Agent Prompt: Edge-AI Smart Traffic Light Controller & Simulator

> **Project Target:** Edge-AI Smart Traffic Light Controller & Simulator (PRJ-009)  
> **Brand Identity:** cl0ud engineering architecture (Apple-style naked glyph lockups)  
> **Lead Systems Architect:** Ojas Singh ([`@Ojas-sta`](https://github.com/Ojas-sta) / `https://github.com/Ojas-sta/cl0ud-brand-engineering`)  
> **Subsystem Hierarchy:**
> - Root: `traffic` (`☁ Traffic`)
> - Density Timing: `traffic-flow` (`☁ Traffic • Flow`)
> - YOLOv8 Vision: `traffic-vision` (`☁ Traffic • Vision`)
> - Emergency Corridor: `traffic-preempt` (`☁ Traffic • Preempt`)
> - Collision & Safety: `traffic-safety` (`☁ Traffic • Safety`)
> - Pedestrian Gate: `traffic-walk` (`☁ Traffic • Walk`)
> - Virtual Simulator: `traffic-sim` (`☁ Traffic • Sim`)
> - Raspberry Pi 4B GPIO: `traffic-gpio` (`☁ Traffic • GPIO`)
> - Priority FSM: `traffic-fsm` (`☁ Traffic • FSM`)

---

## Copy-Paste Prompt for AI Agent (Cursor / Claude / Copilot / Windsurf / Antigravity)

```markdown
You are an expert Edge-AI computer vision engineer and systems architect implementing brand attribution, UI instrumentation, and engineering documentation for the **Edge-AI Smart Traffic Light Controller and Simulator**.

This project is powered by the **cl0ud** engineering ecosystem and co-engineered by **Ojas Singh**.

Your task is to implement the official **cl0ud Subsystem lockups**, badges, and code attributions across this codebase:
1. Virtual Camera Simulator / Pygame / OpenCV Diagnostic HUD window
2. Web Dashboard / Simulation portal (if present)
3. Project `README.md` and documentation
4. Python source files (`controller.py`, `detector.py`, `simulator.py`, `hardware/rpi_gpio.py`)
5. CLI boot banner and telemetry logs

---

### 1. RAW ASSET CDN LINKS

Use these official transparent SVG assets directly:

#### A. White Lockups (Dark Mode / OpenCV / Pygame HUD / Black BG):
- Root Domain: `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/white/cl0ud-traffic.svg`
- Density Timing Engine: `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/white/cl0ud-traffic-flow.svg`
- YOLOv8 Vision: `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/white/cl0ud-traffic-vision.svg`
- Emergency Preemption: `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/white/cl0ud-traffic-preempt.svg`
- Safety & Collision: `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/white/cl0ud-traffic-safety.svg`
- Pedestrian Gate: `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/white/cl0ud-traffic-walk.svg`
- Simulator & HUD: `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/white/cl0ud-traffic-sim.svg`
- Physical GPIO: `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/white/cl0ud-traffic-gpio.svg`
- Priority FSM: `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/white/cl0ud-traffic-fsm.svg`

#### B. Black Lockups (Light Mode / White Docs / Print):
- Replace `/white/` with `/black/` in any of the above URLs.

#### C. Shields.io Badges (For README header):
- Traffic Root: `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/badges/cl0ud-traffic-badge.svg`
- Traffic Flow: `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/badges/cl0ud-traffic-flow-badge.svg`
- Traffic Vision: `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/badges/cl0ud-traffic-vision-badge.svg`
- Traffic Preempt: `https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/badges/cl0ud-traffic-preempt-badge.svg`

---

### 2. IMPLEMENTATION SURFACES

#### Surface 1: README.md Header & Architecture
Add the following badge group directly under the primary title:

```markdown
# 🚦 Edge-AI Smart Traffic Light Controller & Simulator

[![Powered by cl0ud](https://img.shields.io/badge/Powered%20by-cl0ud-00E5FF?style=for-the-badge&logoColor=0B0F19&labelColor=0B0F19)](https://github.com/Ojas-sta/cl0ud-brand-engineering)
[![Co-engineered by Ojas Singh](https://img.shields.io/badge/Co--engineered%20by-Ojas%20Singh-1E3A8A?style=for-the-badge&logoColor=white&labelColor=0B0F19)](https://github.com/Ojas-sta)
[![Subsystem](https://img.shields.io/badge/%E2%98%81%20Traffic-Flow%20%7C%20Vision-00E5FF?style=for-the-badge&logoColor=0B0F19&labelColor=0B0F19)](https://github.com/Ojas-sta/cl0ud-brand-engineering)

<p align="center">
  <a href="https://github.com/Ojas-sta/cl0ud-brand-engineering">
    <img src="https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/white/cl0ud-traffic-flow.svg" alt="cl0ud Traffic Flow Subsystem" height="34" />
  </a>
</p>
```

Add to the Architecture / Subsystems section:
```markdown
### Subsystem Engineering Hierarchy
- **`☁ Traffic.Vision`**: Edge perception pipeline using YOLOv8 with lane & zone classification for North-South and East-West corridors.
- **`☁ Traffic.Flow`**: Deterministic Passenger Car Unit (PCU) density-adaptive green timing: $T_{\text{green}} = \text{clamp}(10 + 1.6 \times \text{PCU}, 10, 50)$ with $\text{PCU} = 0.5 N_{\text{moto}} + 1.0 N_{\text{car}} + 2.5 N_{\text{truck/bus}}$.
- **`☁ Traffic.Preempt`**: Emergency vehicle green corridor preemption (immediate conflicting phase truncation for approaching ambulances and fire trucks).
- **`☁ Traffic.Safety`**: Vision-based junction collision and stasis detection ($\text{IoU} > 0.45 \land v \approx 0$ for $\ge 30$ frames $\rightarrow$ ALL-RED lockdown & automated EMS alert).
- **`☁ Traffic.Walk`**: Vision-based pedestrian queue cutoff gate ($N_{\text{ped}} \ge 5$ triggers $15\text{s}$ walk phase after $25\text{s}$ cooldown).
- **`☁ Traffic.Sim`**: End-to-end 4-way intersection simulation and virtual camera HUD.
- **`☁ Traffic.GPIO`**: Raspberry Pi 4B physical 3-aspect LED and buzzer pinout driver.
- **`☁ Traffic.FSM`**: Non-blocking priority hierarchy decision matrix.
```

#### Surface 2: Pygame / OpenCV Diagnostic HUD Window
In your Pygame / OpenCV simulator display loop (`simulator.py` / `hud.py`), render the cl0ud subsystem watermark in the top-right or bottom diagnostic ribbon:

*For OpenCV:*
```python
# cl0ud Subsystem Diagnostic Overlay
cv2.putText(frame, "cl0ud | Traffic.Flow v1.0", (frame.shape[1] - 260, 28),
            cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 229, 0), 2, cv2.LINE_AA) # BGR Electric Cyan (0, 229, 255)
cv2.putText(frame, "Co-engineered by Ojas Singh", (frame.shape[1] - 260, 48),
            cv2.FONT_HERSHEY_SIMPLEX, 0.45, (180, 180, 180), 1, cv2.LINE_AA)
```

*For Pygame Window Title & HUD:*
```python
pygame.display.set_caption("Edge-AI Smart Traffic Light | Powered by cl0ud | Co-engineered by Ojas Singh")
```

#### Surface 3: Web Dashboard / Status Portal (HTML/React)
If the project includes a web interface or Streamlit dashboard, render the Apple-style lockup in the header or bottom bar:

```html
<footer style="display: flex; justify-content: space-between; align-items: center; padding: 16px 24px; background: #0B0F19; border-top: 1px solid rgba(255,255,255,0.08); font-family: -apple-system, BlinkMacSystemFont, sans-serif;">
  <a href="https://github.com/Ojas-sta/cl0ud-brand-engineering" target="_blank" rel="noopener noreferrer" style="text-decoration: none; display: flex; align-items: center; gap: 8px;">
    <img src="https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/subsystems/white/cl0ud-traffic-flow.svg" alt="cl0ud Traffic Flow" height="26" style="display: block;" />
  </a>
  <span style="font-size: 13px; color: #94A3B8;">
    Co-engineered by <a href="https://github.com/Ojas-sta" style="color: #00E5FF; text-decoration: none; font-weight: 500;">Ojas Singh</a>
  </span>
</footer>
```

#### Surface 4: Python CLI Boot Banner & Source Headers
Add the standard cl0ud engineering banner to `main.py` / `controller.py`:

```python
"""
================================================================================
Edge-AI Smart Traffic Light Controller & Simulator
Subsystem: ☁ Traffic.Flow | ☁ Traffic.Vision | ☁ Traffic.Preempt
Architecture: cl0ud Edge-AI Deterministic Priority Controller
Lead Architect: Ojas Singh (https://github.com/Ojas-sta)
Attribution: Powered by cl0ud | Co-engineered by Ojas Singh
================================================================================
"""

def print_banner():
    print("""
    \033[1;36m============================================================\033[0m
    \033[1;37m   ☁ Traffic.Flow — Edge-AI Smart Traffic Controller        \033[0m
    \033[1;36m============================================================\033[0m
    \033[0;36m   [+] Perception Engine : YOLOv8 Edge (Picamera2 / Virtual)\033[0m
    \033[0;36m   [+] Priority Matrix   : Accident > Emergency > Walk > PCU\033[0m
    \033[0;36m   [+] Hardware Target   : Raspberry Pi 4B (GPIO 17/27/22, 10/9/11)\033[0m
    \033[0;90m   [*] Powered by cl0ud | Co-engineered by Ojas Singh       \033[0m
    \033[1;36m============================================================\033[0m
    """)
```
```
