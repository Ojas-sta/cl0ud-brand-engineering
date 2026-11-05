# cl0ud — Official Subsystem Vector Asset Registry (Apple Lockup Standard)

> **Brand Lockup Standard:** Apple-Style Direct Glyph Lockup (`Pay` / `Card` Paradigm)  
> **Typography:** `-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro", "Outfit"` (Semi-Bold 600)  
> **Optical Metrics:** Height = $1.05\times$ Cap-Height | Kerning Gap = $0.18\times$ Cap-Height | Direct Baseline Anchoring  
> **Colorways:** Solid Black (Light mode / Print), Solid White (Dark mode / OLED), Electric Cyan (Hero UI)  
> **Asset Count:** 440 Total Vector SVGs (110 Black, 110 White, 110 Cyan, 110 Badges)  
> **Generator Script:** [`tools/assets/generate-subsystem-assets.py`](file:///Users/roopalisingh/Desktop/cl0ud/tools/assets/generate-subsystem-assets.py)

---

## 1. Visual Comparison: Apple Pay / Apple Card Standard

```
Pay  (Apple Pay:  Apple Symbol + SF Pro Semibold + 0.18x Cap-Height Gap)
Card (Apple Card: Apple Symbol + SF Pro Semibold + 0.18x Cap-Height Gap)
☁Pay  (cl0ud Pay:  Infinity Symbol + SF Pro Semibold + 0.18x Cap-Height Gap)
☁Card (cl0ud Card: Infinity Symbol + SF Pro Semibold + 0.18x Cap-Height Gap)
```

### Optical Metric Formula
- Symbol Height (Hs): Exactly 1.05 * H_cap
- Kerning Gap (G): Exactly 0.18 * H_cap (tight integrated unit spacing)
- Baseline Offset: 0px (the flat base of the infinity symbol rests exactly on the font baseline)
- Canvas: 100% transparent background with no outer container box or pill frame.

---

## 2. Usage Examples

### Light Mode / Academic Paper / Print (Solid Black)
```markdown
![cl0ud Bedrock](assets/subsystems/black/cl0ud-bedrock.svg)
![cl0ud Wireframe](assets/subsystems/black/cl0ud-wireframe.svg)
![cl0ud Access Latch](assets/subsystems/black/cl0ud-access-latch.svg)
```

### Dark Mode / OLED Display / Keynote (Solid White)
```markdown
![cl0ud Bedrock](assets/subsystems/white/cl0ud-bedrock.svg)
![cl0ud Wireframe](assets/subsystems/white/cl0ud-wireframe.svg)
![cl0ud Access Latch](assets/subsystems/white/cl0ud-access-latch.svg)
```

### Web Hero / Cyan Accent
```markdown
![cl0ud Bedrock](assets/subsystems/cyan/cl0ud-bedrock.svg)
![cl0ud Binzo Holonomic](assets/subsystems/cyan/cl0ud-binzo-holonomic.svg)
```

### GitHub README Status Badges
```markdown
[![cl0ud Bedrock](assets/subsystems/badges/cl0ud-bedrock-badge.svg)](https://github.com/Ojas-sta/cl0ud-brand-engineering)
[![cl0ud Access Latch](assets/subsystems/badges/cl0ud-access-latch-badge.svg)](https://github.com/Ojas-sta/cl0ud-brand-engineering)
```

---

## 3. Master Subsystem Gallery

| ID | Subsystem Name | Domain | Black (Light Mode) | Cyan (Brand Hero) | GitHub Badge | Technical Scope |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `bedrock` | **Bedrock** | Power & Electrical | ![Bedrock Black](black/cl0ud-bedrock.svg) | ![Bedrock Cyan](cyan/cl0ud-bedrock.svg) | ![Bedrock](badges/cl0ud-bedrock-badge.svg) | Isolated Multi-Rail Power & Buck Topology |
| `conduit` | **Conduit** | Power & Electrical | ![Conduit Black](black/cl0ud-conduit.svg) | ![Conduit Cyan](cyan/cl0ud-conduit.svg) | ![Conduit](badges/cl0ud-conduit-badge.svg) | Shielded High-Current Power Harness |
| `strata` | **Strata** | Power & Electrical | ![Strata Black](black/cl0ud-strata.svg) | ![Strata Cyan](cyan/cl0ud-strata.svg) | ![Strata](badges/cl0ud-strata-badge.svg) | Battery State of Health & Impedance Analyzer |
| `haven` | **Haven** | Power & Electrical | ![Haven Black](black/cl0ud-haven.svg) | ![Haven Cyan](cyan/cl0ud-haven.svg) | ![Haven](badges/cl0ud-haven-badge.svg) | Active/Passive Thermal Management |
| `aegis` | **Aegis** | Power & Electrical | ![Aegis Black](black/cl0ud-aegis.svg) | ![Aegis Cyan](cyan/cl0ud-aegis.svg) | ![Aegis](badges/cl0ud-aegis-badge.svg) | Fast Back-EMF & ESD Protection |
| `decouple` | **Decouple** | Power & Electrical | ![Decouple Black](black/cl0ud-decouple.svg) | ![Decouple Cyan](cyan/cl0ud-decouple.svg) | ![Decouple](badges/cl0ud-decouple-badge.svg) | Power Integrity & Inductive Noise Suppression |
| `apex` | **Apex** | Power & Electrical | ![Apex Black](black/cl0ud-apex.svg) | ![Apex Cyan](cyan/cl0ud-apex.svg) | ![Apex](badges/cl0ud-apex-badge.svg) | Peak Motor Torque & Current Limiter |
| `wireframe` | **Wireframe** | Embedded IAC & Wiring | ![Wireframe Black](black/cl0ud-wireframe.svg) | ![Wireframe Cyan](cyan/cl0ud-wireframe.svg) | ![Wireframe](badges/cl0ud-wireframe-badge.svg) | Declarative Pinout Compiler & Netlist Assertions |
| `pinmap` | **Pinmap** | Embedded IAC & Wiring | ![Pinmap Black](black/cl0ud-pinmap.svg) | ![Pinmap Cyan](cyan/cl0ud-pinmap.svg) | ![Pinmap](badges/cl0ud-pinmap-badge.svg) | GPIO Multiplexing & Strapping Pin Conflict Arbiter |
| `busmaster` | **BusMaster** | Embedded IAC & Wiring | ![BusMaster Black](black/cl0ud-busmaster.svg) | ![BusMaster Cyan](cyan/cl0ud-busmaster.svg) | ![BusMaster](badges/cl0ud-busmaster-badge.svg) | Multi-Drop I2C/SPI/UART Bus Arbiter |
| `pulsepwm` | **PulsePWM** | Embedded IAC & Wiring | ![PulsePWM Black](black/cl0ud-pulsepwm.svg) | ![PulsePWM Cyan](cyan/cl0ud-pulsepwm.svg) | ![PulsePWM](badges/cl0ud-pulsepwm-badge.svg) | High-Resolution Hardware Timer & LEDC PWM |
| `matrixkey` | **MatrixKey** | Embedded IAC & Wiring | ![MatrixKey Black](black/cl0ud-matrixkey.svg) | ![MatrixKey Cyan](cyan/cl0ud-matrixkey.svg) | ![MatrixKey](badges/cl0ud-matrixkey-badge.svg) | Debounced Matrix Keypad Scanner |
| `softap` | **SoftAP** | Embedded IAC & Wiring | ![SoftAP Black](black/cl0ud-softap.svg) | ![SoftAP Cyan](cyan/cl0ud-softap.svg) | ![SoftAP](badges/cl0ud-softap-badge.svg) | Offline Captive Portal & Web Server Stack |
| `fsm` | **FSM** | Embedded IAC & Wiring | ![FSM Black](black/cl0ud-fsm.svg) | ![FSM Cyan](cyan/cl0ud-fsm.svg) | ![FSM](badges/cl0ud-fsm-badge.svg) | Deterministic Non-Blocking State Machine |
| `telemetry` | **Telemetry** | Embedded IAC & Wiring | ![Telemetry Black](black/cl0ud-telemetry.svg) | ![Telemetry Cyan](cyan/cl0ud-telemetry.svg) | ![Telemetry](badges/cl0ud-telemetry-badge.svg) | Asynchronous UDP/WebSocket Telemetry Bridge |
| `loom` | **Loom** | Embedded IAC & Wiring | ![Loom Black](black/cl0ud-loom.svg) | ![Loom Cyan](cyan/cl0ud-loom.svg) | ![Loom](badges/cl0ud-loom-badge.svg) | Automated Wiring Harness CAD & Routing |
| `vertex` | **Vertex** | Locomotion & Kinematics | ![Vertex Black](black/cl0ud-vertex.svg) | ![Vertex Cyan](cyan/cl0ud-vertex.svg) | ![Vertex](badges/cl0ud-vertex-badge.svg) | Closed-Form Inverse Kinematics Engine |
| `kinesis` | **Kinesis** | Locomotion & Kinematics | ![Kinesis Black](black/cl0ud-kinesis.svg) | ![Kinesis Cyan](cyan/cl0ud-kinesis.svg) | ![Kinesis](badges/cl0ud-kinesis-badge.svg) | 500Hz Cyclic Real-Time Motor Loop |
| `holodrive` | **HoloDrive** | Locomotion & Kinematics | ![HoloDrive Black](black/cl0ud-holodrive.svg) | ![HoloDrive Cyan](cyan/cl0ud-holodrive.svg) | ![HoloDrive](badges/cl0ud-holodrive-badge.svg) | 4WD Mecanum Omnidirectional Vector Kinematics |
| `breadcrumbs` | **Breadcrumbs** | Locomotion & Kinematics | ![Breadcrumbs Black](black/cl0ud-breadcrumbs.svg) | ![Breadcrumbs Cyan](cyan/cl0ud-breadcrumbs.svg) | ![Breadcrumbs](badges/cl0ud-breadcrumbs-badge.svg) | Spatial Waypoint & Graph Odometry |
| `vector` | **Vector** | Locomotion & Kinematics | ![Vector Black](black/cl0ud-vector.svg) | ![Vector Cyan](cyan/cl0ud-vector.svg) | ![Vector](badges/cl0ud-vector-badge.svg) | Dynamic Window Approach Obstacle Evasion |
| `matrix` | **Matrix** | Locomotion & Kinematics | ![Matrix Black](black/cl0ud-matrix.svg) | ![Matrix Cyan](cyan/cl0ud-matrix.svg) | ![Matrix](badges/cl0ud-matrix-badge.svg) | SE(3) Coordinate Frame Transforms |
| `pilot` | **Pilot** | Locomotion & Kinematics | ![Pilot Black](black/cl0ud-pilot.svg) | ![Pilot Cyan](cyan/cl0ud-pilot.svg) | ![Pilot](badges/cl0ud-pilot-badge.svg) | Autonomous Mission Behavior Trees |
| `tether` | **Tether** | Locomotion & Kinematics | ![Tether Black](black/cl0ud-tether.svg) | ![Tether Cyan](cyan/cl0ud-tether.svg) | ![Tether](badges/cl0ud-tether-badge.svg) | Dynamic Geofence & E-STOP Boundary |
| `horizon` | **Horizon** | Perception & Edge Vision | ![Horizon Black](black/cl0ud-horizon.svg) | ![Horizon Cyan](cyan/cl0ud-horizon.svg) | ![Horizon](badges/cl0ud-horizon-badge.svg) | 3D Point-Cloud Ground-Plane Segmentation |
| `mirador` | **Mirador** | Perception & Edge Vision | ![Mirador Black](black/cl0ud-mirador.svg) | ![Mirador Cyan](cyan/cl0ud-mirador.svg) | ![Mirador](badges/cl0ud-mirador-badge.svg) | Pan-Tilt Stereoscopic Target Tracker |
| `anchor` | **Anchor** | Perception & Edge Vision | ![Anchor Black](black/cl0ud-anchor.svg) | ![Anchor Cyan](cyan/cl0ud-anchor.svg) | ![Anchor](badges/cl0ud-anchor-badge.svg) | Sub-cm AprilTag Optical Localization |
| `visualservo` | **VisualServo** | Perception & Edge Vision | ![VisualServo Black](black/cl0ud-visualservo.svg) | ![VisualServo Cyan](cyan/cl0ud-visualservo.svg) | ![VisualServo](badges/cl0ud-visualservo-badge.svg) | Edge AI Optical Tracking & Proportional Servoing |
| `jukebox` | **Jukebox** | Perception & Edge Vision | ![Jukebox Black](black/cl0ud-jukebox.svg) | ![Jukebox Cyan](cyan/cl0ud-jukebox.svg) | ![Jukebox](badges/cl0ud-jukebox-badge.svg) | Acoustic FFT Bearing Anomaly Detection |
| `macie` | **Macie** | Perception & Edge Vision | ![Macie Black](black/cl0ud-macie.svg) | ![Macie Cyan](cyan/cl0ud-macie.svg) | ![Macie](badges/cl0ud-macie-badge.svg) | Machine-Vision Surface Hazard Classifier |
| `quorum` | **Quorum** | Perception & Edge Vision | ![Quorum Black](black/cl0ud-quorum.svg) | ![Quorum Cyan](cyan/cl0ud-quorum.svg) | ![Quorum](badges/cl0ud-quorum-badge.svg) | Multi-Sensor Kalman Filter Consensus |
| `vanguard` | **Vanguard** | Perception & Edge Vision | ![Vanguard Black](black/cl0ud-vanguard.svg) | ![Vanguard Cyan](cyan/cl0ud-vanguard.svg) | ![Vanguard](badges/cl0ud-vanguard-badge.svg) | 270° Spatial Obstacle Wedge |
| `sentry` | **Sentry** | Perception & Edge Vision | ![Sentry Black](black/cl0ud-sentry.svg) | ![Sentry Cyan](cyan/cl0ud-sentry.svg) | ![Sentry](badges/cl0ud-sentry-badge.svg) | Perimeter Surveillance & Motion Scheduler |
| `spectrum` | **Spectrum** | Perception & Edge Vision | ![Spectrum Black](black/cl0ud-spectrum.svg) | ![Spectrum Cyan](cyan/cl0ud-spectrum.svg) | ![Spectrum](badges/cl0ud-spectrum-badge.svg) | Dynamic Optical Exposure & White Balance |
| `latent` | **Latent** | Simulation & World Models | ![Latent Black](black/cl0ud-latent.svg) | ![Latent Cyan](cyan/cl0ud-latent.svg) | ![Latent](badges/cl0ud-latent-badge.svg) | High-Dimensional JEPA Feature Space Planner |
| `crucible` | **Crucible** | Simulation & World Models | ![Crucible Black](black/cl0ud-crucible.svg) | ![Crucible Cyan](cyan/cl0ud-crucible.svg) | ![Crucible](badges/cl0ud-crucible-badge.svg) | Hardware-in-the-Loop Fault Injector |
| `worldxd` | **WorldXD** | Simulation & World Models | ![WorldXD Black](black/cl0ud-worldxd.svg) | ![WorldXD Cyan](cyan/cl0ud-worldxd.svg) | ![WorldXD](badges/cl0ud-worldxd-badge.svg) | Apple Silicon MPS Physics Simulator |
| `shard` | **Shard** | Simulation & World Models | ![Shard Black](black/cl0ud-shard.svg) | ![Shard Cyan](cyan/cl0ud-shard.svg) | ![Shard](badges/cl0ud-shard-badge.svg) | Spatial World-Mesh Octree Partitioning |
| `parallax` | **Parallax** | Simulation & World Models | ![Parallax Black](black/cl0ud-parallax.svg) | ![Parallax Cyan](cyan/cl0ud-parallax.svg) | ![Parallax](badges/cl0ud-parallax-badge.svg) | Stereo Baseline Depth Disparity Solver |
| `borg` | **Borg** | Distributed Mesh & OS | ![Borg Black](black/cl0ud-borg.svg) | ![Borg Cyan](cyan/cl0ud-borg.svg) | ![Borg](badges/cl0ud-borg-badge.svg) | Lightweight Edge Container Orchestrator |
| `anthos` | **Anthos** | Distributed Mesh & OS | ![Anthos Black](black/cl0ud-anthos.svg) | ![Anthos Cyan](cyan/cl0ud-anthos.svg) | ![Anthos](badges/cl0ud-anthos-badge.svg) | Hybrid Edge-to-Cloud Telemetry Sync |
| `synapse` | **Synapse** | Distributed Mesh & OS | ![Synapse Black](black/cl0ud-synapse.svg) | ![Synapse Cyan](cyan/cl0ud-synapse.svg) | ![Synapse](badges/cl0ud-synapse-badge.svg) | Microcontroller-to-Linux High-Speed IPC |
| `spanner` | **Spanner** | Distributed Mesh & OS | ![Spanner Black](black/cl0ud-spanner.svg) | ![Spanner Cyan](cyan/cl0ud-spanner.svg) | ![Spanner](badges/cl0ud-spanner-badge.svg) | Precision Clock Synchronization (IEEE 1588) |
| `nexus` | **Nexus** | Distributed Mesh & OS | ![Nexus Black](black/cl0ud-nexus.svg) | ![Nexus Cyan](cyan/cl0ud-nexus.svg) | ![Nexus](badges/cl0ud-nexus-badge.svg) | Zero-Config mDNS / Avahi Discovery |
| `pulse` | **Pulse** | Distributed Mesh & OS | ![Pulse Black](black/cl0ud-pulse.svg) | ![Pulse Cyan](cyan/cl0ud-pulse.svg) | ![Pulse](badges/cl0ud-pulse-badge.svg) | Hardware Watchdog & System Heartbeat |
| `genesis` | **Genesis** | Distributed Mesh & OS | ![Genesis Black](black/cl0ud-genesis.svg) | ![Genesis Cyan](cyan/cl0ud-genesis.svg) | ![Genesis](badges/cl0ud-genesis-badge.svg) | Automated Board Provisioning Pipeline |
| `relay` | **Relay** | Distributed Mesh & OS | ![Relay Black](black/cl0ud-relay.svg) | ![Relay Cyan](cyan/cl0ud-relay.svg) | ![Relay](badges/cl0ud-relay-badge.svg) | Galvanically Isolated Solid-State Switching |
| `bigtable` | **Bigtable** | Data & Storage | ![Bigtable Black](black/cl0ud-bigtable.svg) | ![Bigtable Cyan](cyan/cl0ud-bigtable.svg) | ![Bigtable](badges/cl0ud-bigtable-badge.svg) | High-Throughput Binary Telemetry Log |
| `artifact` | **Artifact** | Data & Storage | ![Artifact Black](black/cl0ud-artifact.svg) | ![Artifact Cyan](cyan/cl0ud-artifact.svg) | ![Artifact](badges/cl0ud-artifact-badge.svg) | Immutable CAD & Slicer Hash Registry |
| `chronicle` | **Chronicle** | Data & Storage | ![Chronicle Black](black/cl0ud-chronicle.svg) | ![Chronicle Cyan](cyan/cl0ud-chronicle.svg) | ![Chronicle](badges/cl0ud-chronicle-badge.svg) | SHA-256 Rolling State Audit Trail |
| `vault` | **Vault** | Data & Storage | ![Vault Black](black/cl0ud-vault.svg) | ![Vault Cyan](cyan/cl0ud-vault.svg) | ![Vault](badges/cl0ud-vault-badge.svg) | Hardware Cryptographic Key Vault |
| `ledger` | **Ledger** | Data & Storage | ![Ledger Black](black/cl0ud-ledger.svg) | ![Ledger Cyan](cyan/cl0ud-ledger.svg) | ![Ledger](badges/cl0ud-ledger-badge.svg) | Hardware Cycle & Component Wear Tracker |
| `enclave` | **Enclave** | Data & Storage | ![Enclave Black](black/cl0ud-enclave.svg) | ![Enclave Cyan](cyan/cl0ud-enclave.svg) | ![Enclave](badges/cl0ud-enclave-badge.svg) | Secure OTA Firmware Signature Verifier |
| `echo` | **Echo** | Spatial & Interactive | ![Echo Black](black/cl0ud-echo.svg) | ![Echo Cyan](cyan/cl0ud-echo.svg) | ![Echo](badges/cl0ud-echo-badge.svg) | Offline Conversational Whisper/Piper Voice |
| `musenet` | **MuseNet** | Spatial & Interactive | ![MuseNet Black](black/cl0ud-musenet.svg) | ![MuseNet Cyan](cyan/cl0ud-musenet.svg) | ![MuseNet](badges/cl0ud-musenet-badge.svg) | Expressive Quadruped Choreography |
| `nomad` | **Nomad** | Spatial & Interactive | ![Nomad Black](black/cl0ud-nomad.svg) | ![Nomad Cyan](cyan/cl0ud-nomad.svg) | ![Nomad](badges/cl0ud-nomad-badge.svg) | Autonomous Makerspace Tool Courier |
| `flux` | **Flux** | Spatial & Interactive | ![Flux Black](black/cl0ud-flux.svg) | ![Flux Cyan](cyan/cl0ud-flux.svg) | ![Flux](badges/cl0ud-flux-badge.svg) | Closed-Loop Hydroponic Chemical Dosing |
| `prism` | **Prism** | Spatial & Interactive | ![Prism Black](black/cl0ud-prism.svg) | ![Prism Cyan](cyan/cl0ud-prism.svg) | ![Prism](badges/cl0ud-prism-badge.svg) | Photorealistic Architectural R3F Renderer |
| `sentinel` | **Sentinel** | Spatial & Interactive | ![Sentinel Black](black/cl0ud-sentinel.svg) | ![Sentinel Cyan](cyan/cl0ud-sentinel.svg) | ![Sentinel](badges/cl0ud-sentinel-badge.svg) | 4-Tier Client-Server Anti-Cheat Voting |
| `orbit` | **Orbit** | Spatial & Interactive | ![Orbit Black](black/cl0ud-orbit.svg) | ![Orbit Cyan](cyan/cl0ud-orbit.svg) | ![Orbit](badges/cl0ud-orbit-badge.svg) | 3D Camera Drone Autopilot & Transitions |
| `access` | **Access** | SmartLock Project | ![Access Black](black/cl0ud-access.svg) | ![Access Cyan](cyan/cl0ud-access.svg) | ![Access](badges/cl0ud-access-badge.svg) | Offline-First Physical Access Domain |
| `latch` | **Latch** | SmartLock Project | ![Latch Black](black/cl0ud-latch.svg) | ![Latch Cyan](cyan/cl0ud-latch.svg) | ![Latch](badges/cl0ud-latch-badge.svg) | 50Hz Hardware LEDC PWM Door Servo (GPIO 18) |
| `otp` | **OTP** | SmartLock Project | ![OTP Black](black/cl0ud-otp.svg) | ![OTP Cyan](cyan/cl0ud-otp.svg) | ![OTP](badges/cl0ud-otp-badge.svg) | Single-Use 4-Digit Crypto Passcode (1000-9999) |
| `portal` | **Portal** | SmartLock Project | ![Portal Black](black/cl0ud-portal.svg) | ![Portal Cyan](cyan/cl0ud-portal.svg) | ![Portal](badges/cl0ud-portal-badge.svg) | SoftAP Self-Hosted Web Server (192.168.4.1) |
| `keypad` | **Keypad** | SmartLock Project | ![Keypad Black](black/cl0ud-keypad.svg) | ![Keypad Cyan](cyan/cl0ud-keypad.svg) | ![Keypad](badges/cl0ud-keypad-badge.svg) | Debounced 4x4 Matrix Keypad Scanner (HX543) |
| `feedback` | **Feedback** | SmartLock Project | ![Feedback Black](black/cl0ud-feedback.svg) | ![Feedback Cyan](cyan/cl0ud-feedback.svg) | ![Feedback](badges/cl0ud-feedback-badge.svg) | 16x2 Character I2C LCD Display (0x27) |
| `access-latch` | **Access • Latch** | SmartLock Project | ![Access • Latch Black](black/cl0ud-access-latch.svg) | ![Access • Latch Cyan](cyan/cl0ud-access-latch.svg) | ![Access • Latch](badges/cl0ud-access-latch-badge.svg) | 50Hz Hardware LEDC PWM Door Servo (GPIO 18) |
| `access-otp` | **Access • OTP** | SmartLock Project | ![Access • OTP Black](black/cl0ud-access-otp.svg) | ![Access • OTP Cyan](cyan/cl0ud-access-otp.svg) | ![Access • OTP](badges/cl0ud-access-otp-badge.svg) | Single-Use 4-Digit Crypto Passcode (1000-9999) |
| `access-portal` | **Access • Portal** | SmartLock Project | ![Access • Portal Black](black/cl0ud-access-portal.svg) | ![Access • Portal Cyan](cyan/cl0ud-access-portal.svg) | ![Access • Portal](badges/cl0ud-access-portal-badge.svg) | SoftAP Self-Hosted Web Server (192.168.4.1) |
| `access-keypad` | **Access • Keypad** | SmartLock Project | ![Access • Keypad Black](black/cl0ud-access-keypad.svg) | ![Access • Keypad Cyan](cyan/cl0ud-access-keypad.svg) | ![Access • Keypad](badges/cl0ud-access-keypad-badge.svg) | Debounced 4x4 Matrix Keypad Scanner (HX543) |
| `access-feedback` | **Access • Feedback** | SmartLock Project | ![Access • Feedback Black](black/cl0ud-access-feedback.svg) | ![Access • Feedback Cyan](cyan/cl0ud-access-feedback.svg) | ![Access • Feedback](badges/cl0ud-access-feedback-badge.svg) | 16x2 Character I2C LCD Display (0x27) |
| `access-fsm` | **Access • FSM** | SmartLock Project | ![Access • FSM Black](black/cl0ud-access-fsm.svg) | ![Access • FSM Cyan](cyan/cl0ud-access-fsm.svg) | ![Access • FSM](badges/cl0ud-access-fsm-badge.svg) | Non-Blocking millis() State Machine (5s Timer) |
| `access-iac` | **Access • IAC** | SmartLock Project | ![Access • IAC Black](black/cl0ud-access-iac.svg) | ![Access • IAC Cyan](cyan/cl0ud-access-iac.svg) | ![Access • IAC](badges/cl0ud-access-iac-badge.svg) | Hardware Interconnect & Decoupling Topology |
| `binzo` | **Binzo** | BINZO Robot Project | ![Binzo Black](black/cl0ud-binzo.svg) | ![Binzo Cyan](cyan/cl0ud-binzo.svg) | ![Binzo](badges/cl0ud-binzo-badge.svg) | Autonomous Holonomic Service Robot Base |
| `holonomic` | **Holonomic** | BINZO Robot Project | ![Holonomic Black](black/cl0ud-holonomic.svg) | ![Holonomic Cyan](cyan/cl0ud-holonomic.svg) | ![Holonomic](badges/cl0ud-holonomic-badge.svg) | 4WD Mecanum Wheel Vector Kinematics |
| `sight` | **Sight** | BINZO Robot Project | ![Sight Black](black/cl0ud-sight.svg) | ![Sight Cyan](cyan/cl0ud-sight.svg) | ![Sight](badges/cl0ud-sight-badge.svg) | K210 YOLOv2 Person Detection Visual Servoing |
| `mouth` | **Mouth** | BINZO Robot Project | ![Mouth Black](black/cl0ud-mouth.svg) | ![Mouth Cyan](cyan/cl0ud-mouth.svg) | ![Mouth](badges/cl0ud-mouth-badge.svg) | MG90S Servo Mouth Lid (0° ⇄ 95°) with Chimes |
| `binzo-core` | **Binzo • Core** | BINZO Robot Project | ![Binzo • Core Black](black/cl0ud-binzo-core.svg) | ![Binzo • Core Cyan](cyan/cl0ud-binzo-core.svg) | ![Binzo • Core](badges/cl0ud-binzo-core-badge.svg) | M5Stack Core2 ESP32 & 320x240 LCD Dashboard |
| `binzo-holonomic` | **Binzo • Holonomic** | BINZO Robot Project | ![Binzo • Holonomic Black](black/cl0ud-binzo-holonomic.svg) | ![Binzo • Holonomic Cyan](cyan/cl0ud-binzo-holonomic.svg) | ![Binzo • Holonomic](badges/cl0ud-binzo-holonomic-badge.svg) | 4WD Mecanum Wheel Vector Kinematics |
| `binzo-motordriver` | **Binzo • MotorDriver** | BINZO Robot Project | ![Binzo • MotorDriver Black](black/cl0ud-binzo-motordriver.svg) | ![Binzo • MotorDriver Cyan](cyan/cl0ud-binzo-motordriver.svg) | ![Binzo • MotorDriver](badges/cl0ud-binzo-motordriver-badge.svg) | I2C 4-Channel Motor Encoder Module (0x24) |
| `binzo-patrol` | **Binzo • Patrol** | BINZO Robot Project | ![Binzo • Patrol Black](black/cl0ud-binzo-patrol.svg) | ![Binzo • Patrol Cyan](cyan/cl0ud-binzo-patrol.svg) | ![Binzo • Patrol](badges/cl0ud-binzo-patrol-badge.svg) | Dual TCRT5000 IR Line Follower (Port B L26/R36) |
| `binzo-sight` | **Binzo • Sight** | BINZO Robot Project | ![Binzo • Sight Black](black/cl0ud-binzo-sight.svg) | ![Binzo • Sight Cyan](cyan/cl0ud-binzo-sight.svg) | ![Binzo • Sight](badges/cl0ud-binzo-sight-badge.svg) | K210 YOLOv2 Person Detection Visual Servoing |
| `binzo-mouth` | **Binzo • Mouth** | BINZO Robot Project | ![Binzo • Mouth Black](black/cl0ud-binzo-mouth.svg) | ![Binzo • Mouth Cyan](cyan/cl0ud-binzo-mouth.svg) | ![Binzo • Mouth](badges/cl0ud-binzo-mouth-badge.svg) | MG90S Servo Mouth Lid (0° ⇄ 95°) with Chimes |
| `binzo-telemetry` | **Binzo • Telemetry** | BINZO Robot Project | ![Binzo • Telemetry Black](black/cl0ud-binzo-telemetry.svg) | ![Binzo • Telemetry Cyan](cyan/cl0ud-binzo-telemetry.svg) | ![Binzo • Telemetry](badges/cl0ud-binzo-telemetry-badge.svg) | UDP Radio Telemetry & Joystick Bridge |
| `binzo-fsm` | **Binzo • FSM** | BINZO Robot Project | ![Binzo • FSM Black](black/cl0ud-binzo-fsm.svg) | ![Binzo • FSM Cyan](cyan/cl0ud-binzo-fsm.svg) | ![Binzo • FSM](badges/cl0ud-binzo-fsm-badge.svg) | Autonomous Mission State Flow Machine |
| `expo` | **Expo** | DPSI Expo Project | ![Expo Black](black/cl0ud-expo.svg) | ![Expo Cyan](cyan/cl0ud-expo.svg) | ![Expo](badges/cl0ud-expo-badge.svg) | Spatial 3D Exhibition & Anti-Cheat Voting |
| `hall` | **Hall** | DPSI Expo Project | ![Hall Black](black/cl0ud-hall.svg) | ![Hall Cyan](cyan/cl0ud-hall.svg) | ![Hall](badges/cl0ud-hall-badge.svg) | React Three Fiber Photorealistic 3D Concours |
| `ballot` | **Ballot** | DPSI Expo Project | ![Ballot Black](black/cl0ud-ballot.svg) | ![Ballot Cyan](cyan/cl0ud-ballot.svg) | ![Ballot](badges/cl0ud-ballot-badge.svg) | 4-Tier Anti-Cheat Device Fingerprint Voting |
| `expo-hall` | **Expo • Hall** | DPSI Expo Project | ![Expo • Hall Black](black/cl0ud-expo-hall.svg) | ![Expo • Hall Cyan](cyan/cl0ud-expo-hall.svg) | ![Expo • Hall](badges/cl0ud-expo-hall-badge.svg) | React Three Fiber Photorealistic 3D Concours |
| `expo-tour` | **Expo • Tour** | DPSI Expo Project | ![Expo • Tour Black](black/cl0ud-expo-tour.svg) | ![Expo • Tour Cyan](cyan/cl0ud-expo-tour.svg) | ![Expo • Tour](badges/cl0ud-expo-tour-badge.svg) | 6-Waypoint Automated Camera Drone Tour |
| `expo-synth` | **Expo • Synth** | DPSI Expo Project | ![Expo • Synth Black](black/cl0ud-expo-synth.svg) | ![Expo • Synth Cyan](cyan/cl0ud-expo-synth.svg) | ![Expo • Synth](badges/cl0ud-expo-synth-badge.svg) | Procedural Web Audio Soundscape Synthesizer |
| `expo-pass` | **Expo • Pass** | DPSI Expo Project | ![Expo • Pass Black](black/cl0ud-expo-pass.svg) | ![Expo • Pass Cyan](cyan/cl0ud-expo-pass.svg) | ![Expo • Pass](badges/cl0ud-expo-pass-badge.svg) | HTML5 Canvas Dynamic Innovation Delegate Pass |
| `expo-ballot` | **Expo • Ballot** | DPSI Expo Project | ![Expo • Ballot Black](black/cl0ud-expo-ballot.svg) | ![Expo • Ballot Cyan](cyan/cl0ud-expo-ballot.svg) | ![Expo • Ballot](badges/cl0ud-expo-ballot-badge.svg) | 4-Tier Anti-Cheat Device Fingerprint Voting |
| `cloud` | **Cloud** | Project CLOUD | ![Cloud Black](black/cl0ud-cloud.svg) | ![Cloud Cyan](cyan/cl0ud-cloud.svg) | ![Cloud](badges/cl0ud-cloud-badge.svg) | Autonomous Quadruped Systems Architecture |
| `cloud-kinematics` | **Cloud • Kinematics** | Project CLOUD | ![Cloud • Kinematics Black](black/cl0ud-cloud-kinematics.svg) | ![Cloud • Kinematics Cyan](cyan/cl0ud-cloud-kinematics.svg) | ![Cloud • Kinematics](badges/cl0ud-cloud-kinematics-badge.svg) | 12-DOF Active Joint Quadruped Locomotion |
| `cloud-caddy` | **Cloud • Caddy** | Project CLOUD | ![Cloud • Caddy Black](black/cl0ud-cloud-caddy.svg) | ![Cloud • Caddy Cyan](cyan/cl0ud-cloud-caddy.svg) | ![Cloud • Caddy](badges/cl0ud-cloud-caddy-badge.svg) | Back-Load Guide Rail & 3D Utility Caddy |
| `cloud-power` | **Cloud • Power** | Project CLOUD | ![Cloud • Power Black](black/cl0ud-cloud-power.svg) | ![Cloud • Power Cyan](cyan/cl0ud-cloud-power.svg) | ![Cloud • Power](badges/cl0ud-cloud-power-badge.svg) | 28.8V -> 12V/5V Isolated Electrical Topology |
| `cloud-perception` | **Cloud • Perception** | Project CLOUD | ![Cloud • Perception Black](black/cl0ud-cloud-perception.svg) | ![Cloud • Perception Cyan](cyan/cl0ud-cloud-perception.svg) | ![Cloud • Perception](badges/cl0ud-cloud-perception-badge.svg) | RealSense D435i Depth & 4D LiDAR SLAM |
| `cloud-cognition` | **Cloud • Cognition** | Project CLOUD | ![Cloud • Cognition Black](black/cl0ud-cloud-cognition.svg) | ![Cloud • Cognition Cyan](cyan/cl0ud-cloud-cognition.svg) | ![Cloud • Cognition](badges/cl0ud-cloud-cognition-badge.svg) | Dual-Persona ARGUS & Docent Conversational RAG |
| `loom-iac` | **Loom • IAC** | Embedded IAC & Wiring | ![Loom • IAC Black](black/cl0ud-loom-iac.svg) | ![Loom • IAC Cyan](cyan/cl0ud-loom-iac.svg) | ![Loom • IAC](badges/cl0ud-loom-iac-badge.svg) | Infrastructure-as-Circuit Automated Pinout Header |
| `traffic` | **Traffic** | Smart Traffic Project | ![Traffic Black](black/cl0ud-traffic.svg) | ![Traffic Cyan](cyan/cl0ud-traffic.svg) | ![Traffic](badges/cl0ud-traffic-badge.svg) | Edge-AI Autonomous Urban Traffic Controller |
| `flow` | **Flow** | Smart Traffic Project | ![Flow Black](black/cl0ud-flow.svg) | ![Flow Cyan](cyan/cl0ud-flow.svg) | ![Flow](badges/cl0ud-flow-badge.svg) | PCU Density-Adaptive Timing Engine (alpha=1.6s/PCU) |
| `traffic-flow` | **Traffic • Flow** | Smart Traffic Project | ![Traffic • Flow Black](black/cl0ud-traffic-flow.svg) | ![Traffic • Flow Cyan](cyan/cl0ud-traffic-flow.svg) | ![Traffic • Flow](badges/cl0ud-traffic-flow-badge.svg) | PCU Density-Adaptive Timing Engine (alpha=1.6s/PCU) |
| `traffic-vision` | **Traffic • Vision** | Smart Traffic Project | ![Traffic • Vision Black](black/cl0ud-traffic-vision.svg) | ![Traffic • Vision Cyan](cyan/cl0ud-traffic-vision.svg) | ![Traffic • Vision](badges/cl0ud-traffic-vision-badge.svg) | YOLOv8 Edge Perception & Lane/Zone Classifier |
| `traffic-preempt` | **Traffic • Preempt** | Smart Traffic Project | ![Traffic • Preempt Black](black/cl0ud-traffic-preempt.svg) | ![Traffic • Preempt Cyan](cyan/cl0ud-traffic-preempt.svg) | ![Traffic • Preempt](badges/cl0ud-traffic-preempt-badge.svg) | Emergency Vehicle Priority Preemption (Ambulance Corridor) |
| `traffic-safety` | **Traffic • Safety** | Smart Traffic Project | ![Traffic • Safety Black](black/cl0ud-traffic-safety.svg) | ![Traffic • Safety Cyan](cyan/cl0ud-traffic-safety.svg) | ![Traffic • Safety](badges/cl0ud-traffic-safety-badge.svg) | Collision & Stasis IoU Detector with EMS Dispatch Alert |
| `traffic-walk` | **Traffic • Walk** | Smart Traffic Project | ![Traffic • Walk Black](black/cl0ud-traffic-walk.svg) | ![Traffic • Walk Cyan](cyan/cl0ud-traffic-walk.svg) | ![Traffic • Walk](badges/cl0ud-traffic-walk-badge.svg) | Vision-Based Pedestrian Queue Cutoff Gate (N>=5) |
| `traffic-sim` | **Traffic • Sim** | Smart Traffic Project | ![Traffic • Sim Black](black/cl0ud-traffic-sim.svg) | ![Traffic • Sim Cyan](cyan/cl0ud-traffic-sim.svg) | ![Traffic • Sim](badges/cl0ud-traffic-sim-badge.svg) | Virtual 4-Way Intersection Simulator & Diagnostic HUD |
| `traffic-gpio` | **Traffic • GPIO** | Smart Traffic Project | ![Traffic • GPIO Black](black/cl0ud-traffic-gpio.svg) | ![Traffic • GPIO Cyan](cyan/cl0ud-traffic-gpio.svg) | ![Traffic • GPIO](badges/cl0ud-traffic-gpio-badge.svg) | Raspberry Pi 4B 3-Aspect Physical LED & Buzzer Actuator |
| `traffic-fsm` | **Traffic • FSM** | Smart Traffic Project | ![Traffic • FSM Black](black/cl0ud-traffic-fsm.svg) | ![Traffic • FSM Cyan](cyan/cl0ud-traffic-fsm.svg) | ![Traffic • FSM](badges/cl0ud-traffic-fsm-badge.svg) | Deterministic 4-Phase Priority State Machine |
