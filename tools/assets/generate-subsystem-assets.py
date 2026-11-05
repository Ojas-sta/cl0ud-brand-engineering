#!/usr/bin/env python3
"""
cl0ud Subsystem Asset Generator — Apple Lockup Standard
Generates authentic standalone production SVG assets matching Apple's official
product lockups (Pay, Card) with exact typography, optical kerning, and baseline anchoring.

Output formats:
1. black/  — Solid Black (#000000) on transparent background (for light surfaces & print)
2. white/  — Solid White (#FFFFFF) on transparent background (for dark surfaces & keynotes)
3. cyan/   — Electric Cyan (#00E5FF) on transparent background (signature brand variant)
4. badges/ — Shields.io-style developer badges for GitHub README status bars
"""

import os
import sys
from pathlib import Path
from PIL import ImageFont

CLOUD_PATH = (
    "M 309.8 1.5 c -23.8 3.0 -45.7 11.0 -65.4 23.8 -16.7 10.8 -31.5 24.8 -42.8 40.3 "
    "l -5.5 7.6 -5.1 -1.4 c -7.4 -2.1 -26.8 -2.8 -36.7 -1.3 -39.4 5.7 -70.9 32.3 -83.0 70.0 "
    "l -2.7 8.5 -8.8 6.2 c -38.8 27.0 -59.7 66.9 -59.7 113.8 -0.1 22.0 4.3 40.6 14.2 61.0 "
    "6.8 14.0 15.6 25.8 28.0 37.8 19.9 19.2 41.2 30.5 68.4 36.4 6.9 1.5 13.4 1.8 40.7 1.8 "
    "35.1 -0.0 39.2 -0.4 55.4 -5.7 34.2 -11.0 63.0 -34.9 96.1 -79.7 37.2 -50.3 44.9 -60.4 "
    "55.3 -72.2 22.3 -25.5 45.9 -42.4 72.3 -51.7 11.5 -4.1 22.8 -5.6 35.3 -4.9 11.9 0.7 "
    "19.5 2.6 29.1 7.2 19.6 9.5 33.7 26.4 40.7 48.5 2.0 6.4 2.3 9.5 2.3 21.5 -0.1 13.2 "
    "-0.3 14.5 -3.5 23.9 -7.1 20.9 -21.6 37.0 -41.5 46.2 -14.9 6.9 -13.3 6.7 -83.5 7.2 "
    "l -63.5 0.4 -13.5 18.0 c -7.4 9.9 -18.2 23.4 -23.8 30.0 l -10.4 11.9 90.9 -0.4 "
    "c 89.0 -0.3 91.0 -0.4 99.3 -2.5 19.3 -4.8 31.9 -10.5 49.1 -22.0 47.4 -31.7 69.8 -91.1 "
    "55.6 -147.2 -12.3 -48.2 -49.8 -85.9 -98.0 -98.4 l -9.0 -2.4 -2.3 -9.8 c -2.9 -12.7 "
    "-7.1 -24.0 -13.9 -37.3 -22.0 -42.6 -62.3 -73.3 -109.0 -83.1 -11.5 -2.4 -39.4 -3.5 "
    "-51.1 -2.0 z m 39.2 60.4 c 29.0 6.2 55.4 26.2 68.1 51.9 4.8 9.7 9.7 23.8 8.6 24.7 "
    "-0.5 0.3 -3.3 1.4 -6.3 2.5 -28.5 9.6 -52.0 25.4 -80.5 53.9 -19.7 19.8 -28.6 30.4 "
    "-57.0 68.1 -22.1 29.4 -29.2 38.0 -41.2 49.6 -20.2 19.6 -39.7 29.9 -62.9 33.0 -5.7 0.7 "
    "-16.9 1.0 -31.9 0.6 -19.6 -0.4 -24.1 -0.8 -30.5 -2.6 -45.2 -13.1 -68.8 -61.6 -51.0 "
    "-104.5 9.5 -22.8 26.7 -37.9 51.2 -45.0 l 8.3 -2.4 0.6 -12.8 c 0.6 -15.4 2.9 -23.2 "
    "9.1 -31.5 7.6 -10.2 19.2 -16.8 32.3 -18.4 7.2 -0.8 7.8 -0.1 6.4 7.1 -0.8 4.1 -1.3 29.3 "
    "-1.6 82.2 l -0.4 76.4 3.3 -0.7 c 16.0 -3.5 33.6 -17.1 49.7 -38.7 l 7.2 -9.8 -0.7 -42.2 "
    "c -0.4 -28.7 -0.3 -45.4 0.5 -51.9 3.2 -28.0 16.3 -52.6 37.0 -69.1 13.7 -11.0 32.0 "
    "-19.2 48.6 -21.8 7.8 -1.2 24.2 -0.5 33.1 1.4 z"
)

# Load San Francisco system font or fallback
try:
    SF_FONT = ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", 48)
except Exception:
    try:
        SF_FONT = ImageFont.truetype("/Library/Fonts/Arial.ttf", 48)
    except Exception:
        SF_FONT = None

# Complete Subsystems Definition List
# Format: (id, name, parent, child, category, description)
SUBSYSTEMS = [
    # Power & Electrical Infrastructure
    ("bedrock", "Bedrock", None, None, "Power & Electrical", "Isolated Multi-Rail Power & Buck Topology"),
    ("conduit", "Conduit", None, None, "Power & Electrical", "Shielded High-Current Power Harness"),
    ("strata", "Strata", None, None, "Power & Electrical", "Battery State of Health & Impedance Analyzer"),
    ("haven", "Haven", None, None, "Power & Electrical", "Active/Passive Thermal Management"),
    ("aegis", "Aegis", None, None, "Power & Electrical", "Fast Back-EMF & ESD Protection"),
    ("decouple", "Decouple", None, None, "Power & Electrical", "Power Integrity & Inductive Noise Suppression"),
    ("apex", "Apex", None, None, "Power & Electrical", "Peak Motor Torque & Current Limiter"),

    # Infrastructure-as-Circuit (IAC) & Wiring
    ("wireframe", "Wireframe", None, None, "Embedded IAC & Wiring", "Declarative Pinout Compiler & Netlist Assertions"),
    ("pinmap", "Pinmap", None, None, "Embedded IAC & Wiring", "GPIO Multiplexing & Strapping Pin Conflict Arbiter"),
    ("busmaster", "BusMaster", None, None, "Embedded IAC & Wiring", "Multi-Drop I2C/SPI/UART Bus Arbiter"),
    ("pulsepwm", "PulsePWM", None, None, "Embedded IAC & Wiring", "High-Resolution Hardware Timer & LEDC PWM"),
    ("matrixkey", "MatrixKey", None, None, "Embedded IAC & Wiring", "Debounced Matrix Keypad Scanner"),
    ("softap", "SoftAP", None, None, "Embedded IAC & Wiring", "Offline Captive Portal & Web Server Stack"),
    ("fsm", "FSM", None, None, "Embedded IAC & Wiring", "Deterministic Non-Blocking State Machine"),
    ("telemetry", "Telemetry", None, None, "Embedded IAC & Wiring", "Asynchronous UDP/WebSocket Telemetry Bridge"),
    ("loom", "Loom", None, None, "Embedded IAC & Wiring", "Automated Wiring Harness CAD & Routing"),

    # Locomotion & Kinematics
    ("vertex", "Vertex", None, None, "Locomotion & Kinematics", "Closed-Form Inverse Kinematics Engine"),
    ("kinesis", "Kinesis", None, None, "Locomotion & Kinematics", "500Hz Cyclic Real-Time Motor Loop"),
    ("holodrive", "HoloDrive", None, None, "Locomotion & Kinematics", "4WD Mecanum Omnidirectional Vector Kinematics"),
    ("breadcrumbs", "Breadcrumbs", None, None, "Locomotion & Kinematics", "Spatial Waypoint & Graph Odometry"),
    ("vector", "Vector", None, None, "Locomotion & Kinematics", "Dynamic Window Approach Obstacle Evasion"),
    ("matrix", "Matrix", None, None, "Locomotion & Kinematics", "SE(3) Coordinate Frame Transforms"),
    ("pilot", "Pilot", None, None, "Locomotion & Kinematics", "Autonomous Mission Behavior Trees"),
    ("tether", "Tether", None, None, "Locomotion & Kinematics", "Dynamic Geofence & E-STOP Boundary"),

    # Perception & Edge Vision
    ("horizon", "Horizon", None, None, "Perception & Edge Vision", "3D Point-Cloud Ground-Plane Segmentation"),
    ("mirador", "Mirador", None, None, "Perception & Edge Vision", "Pan-Tilt Stereoscopic Target Tracker"),
    ("anchor", "Anchor", None, None, "Perception & Edge Vision", "Sub-cm AprilTag Optical Localization"),
    ("visualservo", "VisualServo", None, None, "Perception & Edge Vision", "Edge AI Optical Tracking & Proportional Servoing"),
    ("jukebox", "Jukebox", None, None, "Perception & Edge Vision", "Acoustic FFT Bearing Anomaly Detection"),
    ("macie", "Macie", None, None, "Perception & Edge Vision", "Machine-Vision Surface Hazard Classifier"),
    ("quorum", "Quorum", None, None, "Perception & Edge Vision", "Multi-Sensor Kalman Filter Consensus"),
    ("vanguard", "Vanguard", None, None, "Perception & Edge Vision", "270° Spatial Obstacle Wedge"),
    ("sentry", "Sentry", None, None, "Perception & Edge Vision", "Perimeter Surveillance & Motion Scheduler"),
    ("spectrum", "Spectrum", None, None, "Perception & Edge Vision", "Dynamic Optical Exposure & White Balance"),

    # Simulation & World Models
    ("latent", "Latent", None, None, "Simulation & World Models", "High-Dimensional JEPA Feature Space Planner"),
    ("crucible", "Crucible", None, None, "Simulation & World Models", "Hardware-in-the-Loop Fault Injector"),
    ("worldxd", "WorldXD", None, None, "Simulation & World Models", "Apple Silicon MPS Physics Simulator"),
    ("shard", "Shard", None, None, "Simulation & World Models", "Spatial World-Mesh Octree Partitioning"),
    ("parallax", "Parallax", None, None, "Simulation & World Models", "Stereo Baseline Depth Disparity Solver"),

    # Distributed Mesh & Embedded OS
    ("borg", "Borg", None, None, "Distributed Mesh & OS", "Lightweight Edge Container Orchestrator"),
    ("anthos", "Anthos", None, None, "Distributed Mesh & OS", "Hybrid Edge-to-Cloud Telemetry Sync"),
    ("synapse", "Synapse", None, None, "Distributed Mesh & OS", "Microcontroller-to-Linux High-Speed IPC"),
    ("spanner", "Spanner", None, None, "Distributed Mesh & OS", "Precision Clock Synchronization (IEEE 1588)"),
    ("nexus", "Nexus", None, None, "Distributed Mesh & OS", "Zero-Config mDNS / Avahi Discovery"),
    ("pulse", "Pulse", None, None, "Distributed Mesh & OS", "Hardware Watchdog & System Heartbeat"),
    ("genesis", "Genesis", None, None, "Distributed Mesh & OS", "Automated Board Provisioning Pipeline"),
    ("relay", "Relay", None, None, "Distributed Mesh & OS", "Galvanically Isolated Solid-State Switching"),

    # Data Integrity & Storage Vaults
    ("bigtable", "Bigtable", None, None, "Data & Storage", "High-Throughput Binary Telemetry Log"),
    ("artifact", "Artifact", None, None, "Data & Storage", "Immutable CAD & Slicer Hash Registry"),
    ("chronicle", "Chronicle", None, None, "Data & Storage", "SHA-256 Rolling State Audit Trail"),
    ("vault", "Vault", None, None, "Data & Storage", "Hardware Cryptographic Key Vault"),
    ("ledger", "Ledger", None, None, "Data & Storage", "Hardware Cycle & Component Wear Tracker"),
    ("enclave", "Enclave", None, None, "Data & Storage", "Secure OTA Firmware Signature Verifier"),

    # Spatial & Interactive Web
    ("echo", "Echo", None, None, "Spatial & Interactive", "Offline Conversational Whisper/Piper Voice"),
    ("musenet", "MuseNet", None, None, "Spatial & Interactive", "Expressive Quadruped Choreography"),
    ("nomad", "Nomad", None, None, "Spatial & Interactive", "Autonomous Makerspace Tool Courier"),
    ("flux", "Flux", None, None, "Spatial & Interactive", "Closed-Loop Hydroponic Chemical Dosing"),
    ("prism", "Prism", None, None, "Spatial & Interactive", "Photorealistic Architectural R3F Renderer"),
    ("sentinel", "Sentinel", None, None, "Spatial & Interactive", "4-Tier Client-Server Anti-Cheat Voting"),
    ("orbit", "Orbit", None, None, "Spatial & Interactive", "3D Camera Drone Autopilot & Transitions"),

    # ==================== PROJECT HIERARCHICAL SUBSYSTEMS ====================
    # ESP32 SmartLock Access System (PRJ-008)
    ("access", "Access", None, None, "SmartLock Project", "Offline-First Physical Access Domain"),
    ("latch", "Latch", "Access", "Latch", "SmartLock Project", "50Hz Hardware LEDC PWM Door Servo (GPIO 18)"),
    ("otp", "OTP", "Access", "OTP", "SmartLock Project", "Single-Use 4-Digit Crypto Passcode (1000-9999)"),
    ("portal", "Portal", "Access", "Portal", "SmartLock Project", "SoftAP Self-Hosted Web Server (192.168.4.1)"),
    ("keypad", "Keypad", "Access", "Keypad", "SmartLock Project", "Debounced 4x4 Matrix Keypad Scanner (HX543)"),
    ("feedback", "Feedback", "Access", "Feedback", "SmartLock Project", "16x2 Character I2C LCD Display (0x27)"),
    ("access-latch", "Access • Latch", "Access", "Latch", "SmartLock Project", "50Hz Hardware LEDC PWM Door Servo (GPIO 18)"),
    ("access-otp", "Access • OTP", "Access", "OTP", "SmartLock Project", "Single-Use 4-Digit Crypto Passcode (1000-9999)"),
    ("access-portal", "Access • Portal", "Access", "Portal", "SmartLock Project", "SoftAP Self-Hosted Web Server (192.168.4.1)"),
    ("access-keypad", "Access • Keypad", "Access", "Keypad", "SmartLock Project", "Debounced 4x4 Matrix Keypad Scanner (HX543)"),
    ("access-feedback", "Access • Feedback", "Access", "Feedback", "SmartLock Project", "16x2 Character I2C LCD Display (0x27)"),
    ("access-fsm", "Access • FSM", "Access", "FSM", "SmartLock Project", "Non-Blocking millis() State Machine (5s Timer)"),
    ("access-iac", "Access • IAC", "Access", "IAC", "SmartLock Project", "Hardware Interconnect & Decoupling Topology"),

    # BINZO Smart Autonomous Mecanum Robot (PRJ-005)
    ("binzo", "Binzo", None, None, "BINZO Robot Project", "Autonomous Holonomic Service Robot Base"),
    ("holonomic", "Holonomic", "Binzo", "Holonomic", "BINZO Robot Project", "4WD Mecanum Wheel Vector Kinematics"),
    ("sight", "Sight", "Binzo", "Sight", "BINZO Robot Project", "K210 YOLOv2 Person Detection Visual Servoing"),
    ("mouth", "Mouth", "Binzo", "Mouth", "BINZO Robot Project", "MG90S Servo Mouth Lid (0° ⇄ 95°) with Chimes"),
    ("binzo-core", "Binzo • Core", "Binzo", "Core", "BINZO Robot Project", "M5Stack Core2 ESP32 & 320x240 LCD Dashboard"),
    ("binzo-holonomic", "Binzo • Holonomic", "Binzo", "Holonomic", "BINZO Robot Project", "4WD Mecanum Wheel Vector Kinematics"),
    ("binzo-motordriver", "Binzo • MotorDriver", "Binzo", "MotorDriver", "BINZO Robot Project", "I2C 4-Channel Motor Encoder Module (0x24)"),
    ("binzo-patrol", "Binzo • Patrol", "Binzo", "Patrol", "BINZO Robot Project", "Dual TCRT5000 IR Line Follower (Port B L26/R36)"),
    ("binzo-sight", "Binzo • Sight", "Binzo", "Sight", "BINZO Robot Project", "K210 YOLOv2 Person Detection Visual Servoing"),
    ("binzo-mouth", "Binzo • Mouth", "Binzo", "Mouth", "BINZO Robot Project", "MG90S Servo Mouth Lid (0° ⇄ 95°) with Chimes"),
    ("binzo-telemetry", "Binzo • Telemetry", "Binzo", "Telemetry", "BINZO Robot Project", "UDP Radio Telemetry & Joystick Bridge"),
    ("binzo-fsm", "Binzo • FSM", "Binzo", "FSM", "BINZO Robot Project", "Autonomous Mission State Flow Machine"),

    # DPSI Exhibition 2026 Virtual Platform (PRJ-002)
    ("expo", "Expo", None, None, "DPSI Expo Project", "Spatial 3D Exhibition & Anti-Cheat Voting"),
    ("hall", "Hall", "Expo", "Hall", "DPSI Expo Project", "React Three Fiber Photorealistic 3D Concours"),
    ("ballot", "Ballot", "Expo", "Ballot", "DPSI Expo Project", "4-Tier Anti-Cheat Device Fingerprint Voting"),
    ("expo-hall", "Expo • Hall", "Expo", "Hall", "DPSI Expo Project", "React Three Fiber Photorealistic 3D Concours"),
    ("expo-tour", "Expo • Tour", "Expo", "Tour", "DPSI Expo Project", "6-Waypoint Automated Camera Drone Tour"),
    ("expo-synth", "Expo • Synth", "Expo", "Synth", "DPSI Expo Project", "Procedural Web Audio Soundscape Synthesizer"),
    ("expo-pass", "Expo • Pass", "Expo", "Pass", "DPSI Expo Project", "HTML5 Canvas Dynamic Innovation Delegate Pass"),
    ("expo-ballot", "Expo • Ballot", "Expo", "Ballot", "DPSI Expo Project", "4-Tier Anti-Cheat Device Fingerprint Voting"),

    # Project CLOUD Quadruped Robot (PRJ-001)
    ("cloud", "Cloud", None, None, "Project CLOUD", "Autonomous Quadruped Systems Architecture"),
    ("cloud-kinematics", "Cloud • Kinematics", "Cloud", "Kinematics", "Project CLOUD", "12-DOF Active Joint Quadruped Locomotion"),
    ("cloud-caddy", "Cloud • Caddy", "Cloud", "Caddy", "Project CLOUD", "Back-Load Guide Rail & 3D Utility Caddy"),
    ("cloud-power", "Cloud • Power", "Cloud", "Power", "Project CLOUD", "28.8V -> 12V/5V Isolated Electrical Topology"),
    ("cloud-perception", "Cloud • Perception", "Cloud", "Perception", "Project CLOUD", "RealSense D435i Depth & 4D LiDAR SLAM"),
    ("cloud-cognition", "Cloud • Cognition", "Cloud", "Cognition", "Project CLOUD", "Dual-Persona ARGUS & Docent Conversational RAG"),
    ("loom-iac", "Loom • IAC", "Loom", "IAC", "Embedded IAC & Wiring", "Infrastructure-as-Circuit Automated Pinout Header"),

    # Edge-AI Smart Traffic Light System (PRJ-009)
    ("traffic", "Traffic", None, None, "Smart Traffic Project", "Edge-AI Autonomous Urban Traffic Controller"),
    ("flow", "Flow", "Traffic", "Flow", "Smart Traffic Project", "PCU Density-Adaptive Timing Engine (alpha=1.6s/PCU)"),
    ("traffic-flow", "Traffic • Flow", "Traffic", "Flow", "Smart Traffic Project", "PCU Density-Adaptive Timing Engine (alpha=1.6s/PCU)"),
    ("traffic-vision", "Traffic • Vision", "Traffic", "Vision", "Smart Traffic Project", "YOLOv8 Edge Perception & Lane/Zone Classifier"),
    ("traffic-preempt", "Traffic • Preempt", "Traffic", "Preempt", "Smart Traffic Project", "Emergency Vehicle Priority Preemption (Ambulance Corridor)"),
    ("traffic-safety", "Traffic • Safety", "Traffic", "Safety", "Smart Traffic Project", "Collision & Stasis IoU Detector with EMS Dispatch Alert"),
    ("traffic-walk", "Traffic • Walk", "Traffic", "Walk", "Smart Traffic Project", "Vision-Based Pedestrian Queue Cutoff Gate (N>=5)"),
    ("traffic-sim", "Traffic • Sim", "Traffic", "Sim", "Smart Traffic Project", "Virtual 4-Way Intersection Simulator & Diagnostic HUD"),
    ("traffic-gpio", "Traffic • GPIO", "Traffic", "GPIO", "Smart Traffic Project", "Raspberry Pi 4B 3-Aspect Physical LED & Buzzer Actuator"),
    ("traffic-fsm", "Traffic • FSM", "Traffic", "FSM", "Smart Traffic Project", "Deterministic 4-Phase Priority State Machine"),
]

def calculate_text_metrics(text, font_size=48.0):
    """Accurately measure text width using San Francisco system font with fallback."""
    if SF_FONT:
        bbox = SF_FONT.getbbox(text)
        return float(bbox[2] - bbox[0])
    # Fallback character approximation
    char_widths = {
        ' ': 0.28, 'i': 0.28, 'l': 0.28, 'I': 0.30, 't': 0.35, 'f': 0.35, 'r': 0.38,
        'j': 0.32, '•': 0.45, 'm': 0.82, 'w': 0.80, 'M': 0.86, 'W': 0.90,
        'A': 0.66, 'B': 0.64, 'C': 0.66, 'D': 0.68, 'E': 0.62, 'F': 0.58,
        'G': 0.70, 'H': 0.70, 'K': 0.66, 'N': 0.70, 'O': 0.72, 'P': 0.62,
        'R': 0.66, 'S': 0.62, 'T': 0.58, 'U': 0.70, 'V': 0.64, 'X': 0.64,
        'Y': 0.62, 'Z': 0.62
    }
    w = 0.0
    for ch in text:
        w += char_widths.get(ch, 0.56) * font_size
    return w

def generate_apple_lockup_svg(sub_id, display_name, parent, child, color_mode="black"):
    """
    Generate naked Apple-style lockup (Pay / Card style).
    No background box. Pure vector mark + text on transparent canvas.
    Exact metrics:
      - Font size: 48px
      - Cap-Height H: ~36px
      - Symbol Height Hs: 1.05 * H = 37.8px
      - Symbol Width Ws: 55.3px (from 593:405.1 ratio)
      - Optical Gap G: 0.18 * H = 6.5px (tight Apple kerning)
      - Baseline Alignment: Bottom of cloud matches baseline of text
    """
    font_size = 48.0
    cap_height = 36.0
    symbol_height = 1.05 * cap_height  # 37.8px
    symbol_scale = symbol_height / 405.1  # 0.09331
    symbol_width = 593.0 * symbol_scale  # 55.33px
    optical_gap = 6.5  # tight Apple spacing

    # Determine colors
    if color_mode == "black":
        fill_color = "#000000"
        child_color = "#475569"
        sep_color = "#000000"
        grad_def = ""
        symbol_fill = "#000000"
    elif color_mode == "white":
        fill_color = "#FFFFFF"
        child_color = "#94A3B8"
        sep_color = "#FFFFFF"
        grad_def = ""
        symbol_fill = "#FFFFFF"
    elif color_mode == "cyan":
        fill_color = "#F8FAFC"
        child_color = "#94A3B8"
        sep_color = "#00E5FF"
        grad_def = f"""  <defs>
    <linearGradient id="cyanGrad-{sub_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>
  </defs>"""
        symbol_fill = f"url(#cyanGrad-{sub_id})"

    # Calculate exact text width
    if parent and child:
        w_parent = calculate_text_metrics(parent, font_size)
        w_sep = calculate_text_metrics(" • ", font_size)
        w_child = calculate_text_metrics(child, font_size)
        total_text_width = w_parent + w_sep + w_child
    else:
        total_text_width = calculate_text_metrics(display_name, font_size)

    # Canvas dimensions
    padding_left = 2.0
    padding_right = 4.0
    total_width = padding_left + symbol_width + optical_gap + total_text_width + padding_right
    total_height = 58.0

    # Vertical positioning: baseline at Y = 44.0
    baseline_y = 44.0
    symbol_y = baseline_y - symbol_height
    symbol_x = padding_left

    # Text positioning
    text_start_x = padding_left + symbol_width + optical_gap

    if parent and child:
        x_parent = text_start_x
        x_sep = x_parent + w_parent
        x_child = x_sep + w_sep
        text_element = f"""  <text x="{x_parent:.1f}" y="{baseline_y:.1f}" class="lockup-parent" fill="{fill_color}">{parent}</text>
  <text x="{x_sep:.1f}" y="{baseline_y:.1f}" class="lockup-sep" fill="{sep_color}"> • </text>
  <text x="{x_child:.1f}" y="{baseline_y:.1f}" class="lockup-child" fill="{child_color}">{child}</text>"""
    else:
        text_element = f"""  <text x="{text_start_x:.1f}" y="{baseline_y:.1f}" class="lockup-parent" fill="{fill_color}">{display_name}</text>"""

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_width:.1f} {total_height:.1f}" width="{total_width:.1f}" height="{total_height:.1f}" fill="none">
  <!-- cl0ud Apple-Style Lockup: {display_name} ({color_mode.capitalize()}) -->
{grad_def}
  <style>
    .lockup-parent {{
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro", "Outfit", "Helvetica Neue", sans-serif;
      font-size: {font_size:.1f}px;
      font-weight: 600;
      letter-spacing: -0.025em;
    }}
    .lockup-sep {{
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro", sans-serif;
      font-size: {font_size:.1f}px;
      font-weight: 700;
    }}
    .lockup-child {{
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro", "Outfit", "Helvetica Neue", sans-serif;
      font-size: {font_size:.1f}px;
      font-weight: 500;
      letter-spacing: -0.015em;
    }}
  </style>

  <!-- Infinity Cloud Symbol -->
  <g transform="translate({symbol_x:.1f}, {symbol_y:.1f}) scale({symbol_scale:.4f})" fill="{symbol_fill}">
    <path fill-rule="evenodd" d="{CLOUD_PATH}"/>
  </g>

  <!-- Product Name -->
{text_element}
</svg>"""
    return svg

def generate_badge_svg(sub_id, display_name, parent, child, category, description):
    """Generate GitHub README badge matching Shields.io standards."""
    font_size = 11.0
    left_width = 32.0
    text_width = calculate_text_metrics(display_name, font_size) + 18.0
    text_width = max(text_width, 48.0)
    total_width = left_width + text_width
    height = 24.0

    icon_h = 14.0
    icon_scale = icon_h / 408.0
    icon_w = 608.0 * icon_scale
    icon_x = (left_width - icon_w) / 2.0
    icon_y = (height - icon_h) / 2.0
    text_x = left_width + (text_width / 2.0)
    text_y = 16.0

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_width:.1f} {height:.1f}" width="{total_width:.1f}" height="{height:.1f}">
  <!-- cl0ud Badge: {display_name} -->
  <defs>
    <linearGradient id="badgeCyan-{sub_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>
  </defs>

  <g shape-rendering="crispEdges">
    <path fill="#0B0F19" d="M0 0 h{left_width:.1f} v{height:.1f} H0 z"/>
    <path fill="#0F172A" d="M{left_width:.1f} 0 h{text_width:.1f} v{height:.1f} H{left_width:.1f} z"/>
  </g>

  <rect x="0.5" y="0.5" width="{total_width - 1.0:.1f}" height="{height - 1.0:.1f}" rx="4" fill="none" stroke="#1E293B" stroke-width="1"/>

  <g transform="translate({icon_x:.1f}, {icon_y:.1f}) scale({icon_scale:.4f})" fill="url(#badgeCyan-{sub_id})">
    <path fill-rule="evenodd" d="{CLOUD_PATH}"/>
  </g>

  <text x="{text_x:.1f}" y="{text_y:.1f}" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Outfit', sans-serif" font-size="{font_size}px" font-weight="600" fill="#00E5FF" letter-spacing="-0.01em">{display_name}</text>
</svg>"""
    return svg

def main():
    root = Path(__file__).resolve().parent.parent.parent
    subsystems_dir = root / "assets" / "subsystems"
    black_dir = subsystems_dir / "black"
    white_dir = subsystems_dir / "white"
    cyan_dir = subsystems_dir / "cyan"
    badges_dir = subsystems_dir / "badges"

    black_dir.mkdir(parents=True, exist_ok=True)
    white_dir.mkdir(parents=True, exist_ok=True)
    cyan_dir.mkdir(parents=True, exist_ok=True)
    badges_dir.mkdir(parents=True, exist_ok=True)

    print("==================================================")
    print("cl0ud Apple-Style Subsystem Asset Generator")
    print(f"Total Subsystems: {len(SUBSYSTEMS)}")
    print(f"Output: {subsystems_dir}")
    print("==================================================")

    readme_rows = []

    for sub_id, name, parent, child, cat, desc in SUBSYSTEMS:
        filename = f"cl0ud-{sub_id}.svg"
        badge_filename = f"cl0ud-{sub_id}-badge.svg"

        # Generate Black (for light surfaces)
        svg_black = generate_apple_lockup_svg(sub_id, name, parent, child, "black")
        with open(black_dir / filename, "w", encoding="utf-8") as f:
            f.write(svg_black)

        # Generate White (for dark surfaces)
        svg_white = generate_apple_lockup_svg(sub_id, name, parent, child, "white")
        with open(white_dir / filename, "w", encoding="utf-8") as f:
            f.write(svg_white)

        # Generate Cyan (Electric Cyan signature)
        svg_cyan = generate_apple_lockup_svg(sub_id, name, parent, child, "cyan")
        with open(cyan_dir / filename, "w", encoding="utf-8") as f:
            f.write(svg_cyan)

        # Generate Developer Badge
        svg_badge = generate_badge_svg(sub_id, name, parent, child, cat, desc)
        with open(badges_dir / badge_filename, "w", encoding="utf-8") as f:
            f.write(svg_badge)

        readme_rows.append(
            f"| `{sub_id}` | **{name}** | {cat} | ![{name} Black](black/{filename}) | ![{name} Cyan](cyan/{filename}) | ![{name}](badges/{badge_filename}) | {desc} |"
        )

    # Master README
    readme_content = f"""# cl0ud — Official Subsystem Vector Asset Registry (Apple Lockup Standard)

> **Brand Lockup Standard:** Apple-Style Direct Glyph Lockup (`Pay` / `Card` Paradigm)  
> **Typography:** `-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro", "Outfit"` (Semi-Bold 600)  
> **Optical Metrics:** Height = $1.05\\times$ Cap-Height | Kerning Gap = $0.18\\times$ Cap-Height | Direct Baseline Anchoring  
> **Colorways:** Solid Black (Light mode / Print), Solid White (Dark mode / OLED), Electric Cyan (Hero UI)  
> **Asset Count:** {len(SUBSYSTEMS) * 4} Total Vector SVGs ({len(SUBSYSTEMS)} Black, {len(SUBSYSTEMS)} White, {len(SUBSYSTEMS)} Cyan, {len(SUBSYSTEMS)} Badges)  
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
""" + "\n".join(readme_rows) + """
"""

    with open(subsystems_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print(f"Generated {len(SUBSYSTEMS)} Black SVGs in {black_dir}")
    print(f"Generated {len(SUBSYSTEMS)} White SVGs in {white_dir}")
    print(f"Generated {len(SUBSYSTEMS)} Cyan SVGs in {cyan_dir}")
    print(f"Generated {len(SUBSYSTEMS)} Badge SVGs in {badges_dir}")
    print(f"Total: {len(SUBSYSTEMS) * 4} production assets created successfully.")

if __name__ == "__main__":
    main()
