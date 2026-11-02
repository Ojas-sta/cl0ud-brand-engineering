# Exhibition Project Case Study — Project CLOUD

[![Platform](https://img.shields.io/badge/Platform-Unitree%20Go2%20Edu-000000?style=for-the-badge)](https://www.unitree.com/)
[![Powered by cl0ud](https://img.shields.io/badge/Powered%20by-cl0ud-00E5FF?style=for-the-badge&logoColor=0B0F19&labelColor=0B0F19)](https://github.com/Ojas-sta/cl0ud-brand-engineering)
[![Co-engineered by Ojas Singh](https://img.shields.io/badge/Co--engineered%20by-Ojas%20Singh-1E3A8A?style=for-the-badge&logoColor=white&labelColor=0B0F19)](https://github.com/Ojas-sta)

> **Exhibition Context:** DPSI Tech & Innovation Exhibition 2026  
> **System Designation:** CLOUD (Cognitive Laboratory Operations & Utility Dispatcher)  
> **Dual Personas:** ARGUS (Makerspace Steward) & THE DOCENT (VIP Tour Guide)  
> **Source Repository:** [`https://github.com/Ojas-sta/Cloud_DPSI-EXPO26`](https://github.com/Ojas-sta/Cloud_DPSI-EXPO26)

---

## 1. Project Background
Project CLOUD was engineered for the DPS Indirapuram Annual Exhibition as both a physical demonstration of high-level quadruped kinematics and an operational makerspace utility tool.

```mermaid
sequenceDiagram
    participant Evaluator as VIP Evaluator / Judge
    participant Docent as THE DOCENT (Unitree Go2)
    participant Sensors as RealSense D435i / LiDAR
    participant Audio as Local RAG & Piper TTS

    Evaluator->>Docent: Approaches exhibition booth
    Sensors->>Docent: Detects visitor within 1.5m social envelope
    Docent->>Docent: Kinematic 180° presenter pivot
    Docent->>Audio: Queries local RAG for project overview
    Audio->>Evaluator: Speaks conversational technical monograph narration
```

---

## 2. Key Engineering Highlights
- **Custom Back-Load Guide Rail Mounting:** Vibration-dampened mechanical interface mounted with 8x M4 guide rail screws into the Go2 structural spine.
- **Dual-Bay Utility Caddy:** PETG rapid-prototyped tool holder with magnetic retention.
- **Isolated Power Distribution:** Step-down buck regulation with TVS surge protection.

---

## 3. Exhibition Attribution Plinth
Mounted directly to the robot chassis spine:
```text
SYSTEMS ARCHITECTURE: Powered by cl0ud
CO-ENGINEERED BY:     Ojas Singh
HOST TEAM:            DPSI Student Robotics Team
ACADEMIC LAB:         Advanced Prototyping Center, DPS Indirapuram
```
