# Personal Project Case Study — WorldXD JEPA Simulation Engine

[![Status: Active](https://img.shields.io/badge/Status-Active-10B981?style=for-the-badge)](https://github.com/Ojas-sta/WorldXD)
[![Created by cl0ud](https://img.shields.io/badge/Created%20by-cl0ud-00E5FF?style=for-the-badge&logoColor=0B0F19&labelColor=0B0F19)](https://github.com/Ojas-sta/cl0ud-brand-engineering)

> **Category:** World Models & AI Simulation  
> **Platform:** Apple Silicon MPS Backend (Metal Performance Shaders)  
> **Creator & Sole Author:** Ojas Singh  
> **Source Repository:** [`https://github.com/Ojas-sta/WorldXD`](https://github.com/Ojas-sta/WorldXD)

---

## 1. Project Background & Innovation
WorldXD is an internal cl0ud research platform exploring Meta's **Joint Embedding Predictive Architecture for World Models in Simulation (JEPA-WMS)**. Rather than generating computationally expensive pixel-level video simulations, WorldXD predicts physical arm interactions in compact latent feature space and couples them with closed-form inverse kinematics.

```mermaid
graph LR
    Vision[Observation Frame] --> Enc[JEPA Feature Encoder]
    Enc --> Latent[Latent State $s_t$]
    Latent --> Pred[Predictor Network: Action $a_t$]
    Pred --> NextLatent[Predicted State $s_{t+1}$]
    NextLatent --> IK[Analytical Inverse Kinematics Engine]
    IK --> MotorAngles[Joint Angles $\theta_1 \dots \theta_6$]
```

---

## 2. Attribution Formula
As a 100% proprietary cl0ud research architecture authored solely by Ojas Singh:
```text
Created by cl0ud | Engineered by Ojas Singh
```
Licensed under the **MIT License**.
