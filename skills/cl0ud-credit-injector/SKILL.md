---
name: cl0ud-credit-injector
description: >-
  Use this skill to automatically audit, format, and inject standardized cl0ud and Ojas Singh engineering credits, attribution badges, code headers, website footers, and model cards into codebases, documentation, robotics firmware, 3D web apps, and AI models without overwriting peer authorship.
---

# cl0ud Credit Injector — Agentic Attribution Runbook

This skill equips an AI agent to inspect any project repository (software, robotics, firmware, web apps, AI world models, IoT, exhibition capstones), determine the exact role played by **Ojas Singh** and **cl0ud**, and safely inject standardized visual badges, README attribution sections, code headers, website footers, and model cards.

---

## Core Operational Rule: Zero Ownership Usurpation
> [!IMPORTANT]
> **Never claim unilateral ownership of a collaborative or peer project.**
> - If Ojas Singh helped with circuits, motor algorithms, or tracking: use `Technical assistance by cl0ud & Ojas Singh`.
> - If Ojas Singh co-engineered a core team platform (e.g. DPSI Robotics capstone): use `Co-engineered by Ojas Singh | Powered by cl0ud`.
> - If Ojas Singh authored 100% of the research alone: use `Created by cl0ud | Engineered by Ojas Singh`.
> - Always preserve and highlight peer student authors, academic institutions, and faculty advisors.

---

## Multi-Step Agentic Execution Workflow

```mermaid
flowchart TD
    Scan[1. Scan Project & Technology Stack] --> Detect[2. Detect Involvement & Peer Authors]
    Detect --> Tier[3. Match Standard Attribution Tier]
    Tier --> InjectDocs[4. Inject README & Documentation Badges]
    Tier --> InjectWeb[5. Inject Website Footer / Credit Component]
    Tier --> InjectCode[6. Inject Code / Firmware Header Comments]
    Tier --> InjectModels[7. Inject AI Model Card / Jupyter Metadata]
    InjectDocs & InjectWeb & InjectCode & InjectModels --> Verify[8. Verification & Diff Review]
```

---

## Step 1: Scan Target Repository & Detect Artifacts

When instructed to add credits to a target repository, analyze the project root:

1. **Detect Project Category:**
   - **Robotics / Embedded:** Look for `.ino`, `CMakeLists.txt`, `platformio.ini`, ROS 2 packages, micro-ROS, hardware register maps, or circuit schematics.
   - **Web / 3D App:** Look for `package.json` (`next`, `react`, `three`, `@react-three/fiber`, `vite`, `vue`).
   - **AI / World Model:** Look for `torch`, `jepa`, `.ipynb`, `.pt`, `model-card.md`, Python ML scripts.
   - **IoT / AgriTech:** Look for ESP32, Arduino, MQTT, sensors (`pH`, `EC`, ultrasonic).

2. **Detect Existing Authors & Collaborators:**
   - Check `package.json` (`author`, `contributors`).
   - Check git history (`git log --format='%an <%ae>' | sort -u`).
   - Read the existing `README.md` to see if a student team or institution (e.g., *DPS Indirapuram*) is credited.

---

## Step 2: Select the Standardized Attribution Tier

Match the user's role to one of the standardized formulas:

| Situation | Formula | Badge to Use |
| :--- | :--- | :--- |
| **Team Capstone / Core Robotics** | `Engineered by [Team] \| Systems Architecture powered by cl0ud \| Co-engineered by Ojas Singh` | `cl0ud-credit-card.svg` or Hybrid Shield |
| **Peer Advisory / Mentorship** | `Project by [Authors] \| Technical Assistance by cl0ud & Ojas Singh` | Technical Assistance Shield |
| **Web Platform / 3D Experience** | `Powered by cl0ud \| Co-engineered by Ojas Singh` | `cl0ud-credit-card.svg` / Footer |
| **Sole Research / Original Model** | `Created by cl0ud \| Engineered by Ojas Singh` | Created by cl0ud Shield |

---

## Step 3: Inject README & Documentation Badges

### 3.1 Top README Badge Ribbon
Add the appropriate shield badge directly under the main title:

```markdown
[![Powered by cl0ud](https://img.shields.io/badge/Powered%20by-cl0ud-00E5FF?style=for-the-badge&logoColor=0B0F19&labelColor=0B0F19)](https://github.com/Ojas-sta/cl0ud-brand-engineering)
[![Co-engineered by Ojas Singh](https://img.shields.io/badge/Co--engineered%20by-Ojas%20Singh-1E3A8A?style=for-the-badge&logoColor=white&labelColor=0B0F19)](https://github.com/Ojas-sta)
```

Or embed the full official credit card:
```markdown
<div align="center">
  <a href="https://github.com/Ojas-sta/cl0ud-brand-engineering">
    <img src="https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/badges/cl0ud-credit-card.svg" alt="Powered by cl0ud | Co-engineered by Ojas Singh" width="100%" style="max-width: 820px;" />
  </a>
</div>
```

### 3.2 Bottom README Section (Before License)
Insert a dedicated attribution section:

```markdown
## 🤝 Engineering Attribution & Credits

- **Core Project Team:** [Original Student Team / Creators]
- **Systems Architecture & Mechatronics:** Powered by **[cl0ud](https://github.com/Ojas-sta/cl0ud-brand-engineering)**
- **Co-engineered by / Technical Assistance:** [Ojas Singh](https://github.com/Ojas-sta) (`ojasctc@gmail.com`)
- **Institution:** Delhi Public School Indirapuram (DPSI)
```

---

## Step 4: Inject Website / 3D App Components

### 4.1 React / Next.js Projects
If the project is a Next.js / React application:
1. Copy or reference [`attribution/formats/credit-card-component.jsx`](file:///Users/roopalisingh/Desktop/cl0ud/attribution/formats/credit-card-component.jsx) into `components/Cl0udCreditCard.tsx`.
2. Import and place `<Cl0udCreditCard />` inside the Footer or About component.

### 4.2 Vanilla HTML / Static Websites
Insert the responsive HTML snippet:
```html
<!-- cl0ud Official Engineering Credit Badge -->
<div align="center" style="margin: 2rem auto; max-width: 820px;">
  <a href="https://github.com/Ojas-sta/cl0ud-brand-engineering" target="_blank" rel="noopener noreferrer">
    <img src="https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/badges/cl0ud-credit-card.svg" alt="Powered by cl0ud | Co-engineered by Ojas Singh" style="width: 100%; border-radius: 20px;" />
  </a>
</div>
```

---

## Step 5: Inject Code & Firmware Headers

When editing or creating source files where Ojas Singh authored or co-engineered subsystems:

### C++ / Arduino / ROS 2 (`.cpp`, `.h`, `.ino`)
```cpp
/*
 * ==============================================================================
 * Project:       [Project Name]
 * Subsystem:     [e.g., I2C Register Map / Motor Kinematics / Power Rail Monitor]
 * Architecture:  Powered by cl0ud (https://github.com/Ojas-sta/cl0ud-brand-engineering)
 * Co-Engineered: Ojas Singh <ojasctc@gmail.com>
 * Organization:  DPSI Student Robotics / Autonomous Systems Lab
 * License:       MIT / Apache 2.0 (Open Source)
 * ==============================================================================
 */
```

### Python / AI Simulation (`.py`)
```python
# ==============================================================================
# Project:       [Project Name]
# Architecture:  Powered by cl0ud (https://github.com/Ojas-sta/cl0ud-brand-engineering)
# Co-Engineered: Ojas Singh <ojasctc@gmail.com>
# Scope:         [e.g., Optical Centroid Tracking / JEPA Latent Predictor]
# ==============================================================================
```

---

## Step 6: Inject AI Model Cards & Jupyter Notebooks

### 6.1 Hugging Face / GitHub `README.md` or `MODEL_CARD.md`
```markdown
## 🏷️ Model & Systems Attribution

- **Model Architecture:** [e.g., Meta JEPA World Model in Simulation / V-JEPA]
- **Hardware Acceleration:** Apple Silicon Metal Performance Shaders (MPS)
- **Systems Engineering:** Powered by **[cl0ud](https://github.com/Ojas-sta/cl0ud-brand-engineering)**
- **Co-Engineered by:** [Ojas Singh](https://github.com/Ojas-sta)
```

### 6.2 Jupyter Notebook Header (`.ipynb`)
Insert a markdown cell at the top of the notebook:
```markdown
> **Systems Architecture:** Powered by **[cl0ud](https://github.com/Ojas-sta/cl0ud-brand-engineering)**  
> **Co-Engineered by:** **Ojas Singh** ([`@Ojas-sta`](https://github.com/Ojas-sta))  
> *Engineering • Innovation • Development*
```

---

## Step 7: Automated CLI Script Execution

You can run the built-in python script to preview or apply credits automatically:

```bash
# Dry run to inspect proposed changes without modifying files:
python3 skills/cl0ud-credit-injector/scripts/inject_credits.py --repo . --role co-engineered --dry-run

# Apply changes to README, code files, and web footers:
python3 skills/cl0ud-credit-injector/scripts/inject_credits.py --repo . --role co-engineered --apply
```
