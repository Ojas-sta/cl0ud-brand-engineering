#!/usr/bin/env python3
"""
cl0ud Subsystem Asset Generator
Generates standalone production SVG assets (Apple-style lockups and GitHub README badges)
for all cl0ud root subsystems and hierarchical nested sub-subsystems.
"""

import os
import sys
from pathlib import Path

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
    ("access-latch", "Access • Latch", "Access", "Latch", "SmartLock Project", "50Hz Hardware LEDC PWM Door Servo (GPIO 18)"),
    ("access-otp", "Access • OTP", "Access", "OTP", "SmartLock Project", "Single-Use 4-Digit Crypto Passcode (1000-9999)"),
    ("access-portal", "Access • Portal", "Access", "Portal", "SmartLock Project", "SoftAP Self-Hosted Web Server (192.168.4.1)"),
    ("access-keypad", "Access • Keypad", "Access", "Keypad", "SmartLock Project", "Debounced 4x4 Matrix Keypad Scanner (HX543)"),
    ("access-feedback", "Access • Feedback", "Access", "Feedback", "SmartLock Project", "16x2 Character I2C LCD Display (0x27)"),
    ("access-fsm", "Access • FSM", "Access", "FSM", "SmartLock Project", "Non-Blocking millis() State Machine (5s Timer)"),
    ("access-iac", "Access • IAC", "Access", "IAC", "SmartLock Project", "Hardware Interconnect & Decoupling Topology"),

    # BINZO Smart Autonomous Mecanum Robot (PRJ-005)
    ("binzo", "Binzo", None, None, "BINZO Robot Project", "Autonomous Holonomic Service Robot Base"),
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
    ("expo-hall", "Expo • Hall", "Expo", "Hall", "DPSI Expo Project", "React Three Fiber Photorealistic 3D Concours"),
    ("expo-tour", "Expo • Tour", "Expo", "Tour", "DPSI Expo Project", "6-Waypoint Automated Camera Drone Tour"),
    ("expo-synth", "Expo • Synth", "Expo", "Synth", "DPSI Expo Project", "Procedural Web Audio Soundscape Synthesizer"),
    ("expo-pass", "Expo • Pass", "Expo", "Pass", "DPSI Expo Project", "HTML5 Canvas Dynamic Innovation Delegate Pass"),
    ("expo-ballot", "Expo • Ballot", "Expo", "Ballot", "DPSI Expo Project", "4-Tier Anti-Cheat Device Fingerprint Voting"),

    # Project CLOUD Quadruped Robot (PRJ-001)
    ("cloud-kinematics", "Cloud • Kinematics", "Cloud", "Kinematics", "Project CLOUD", "12-DOF Active Joint Quadruped Locomotion"),
    ("cloud-caddy", "Cloud • Caddy", "Cloud", "Caddy", "Project CLOUD", "Back-Load Guide Rail & 3D Utility Caddy"),
    ("cloud-power", "Cloud • Power", "Cloud", "Power", "Project CLOUD", "28.8V -> 12V/5V Isolated Electrical Topology"),
    ("cloud-perception", "Cloud • Perception", "Cloud", "Perception", "Project CLOUD", "RealSense D435i Depth & 4D LiDAR SLAM"),
    ("cloud-cognition", "Cloud • Cognition", "Cloud", "Cognition", "Project CLOUD", "Dual-Persona ARGUS & Docent Conversational RAG"),

    # Loom IAC & Wiring
    ("loom-iac", "Loom • IAC", "Loom", "IAC", "Embedded IAC & Wiring", "Infrastructure-as-Circuit Automated Pinout Header"),
]

def estimate_text_width(text, font_size=20):
    """Estimate pixel width for text rendered with Outfit font."""
    char_widths = {
        ' ': 0.28, 'i': 0.30, 'l': 0.30, 'I': 0.32, 't': 0.38, 'f': 0.38, 'r': 0.42,
        'j': 0.35, '•': 0.45, 'm': 0.82, 'w': 0.80, 'M': 0.88, 'W': 0.92,
        'A': 0.68, 'B': 0.66, 'C': 0.68, 'D': 0.70, 'E': 0.64, 'F': 0.60,
        'G': 0.72, 'H': 0.72, 'K': 0.68, 'N': 0.72, 'O': 0.74, 'P': 0.64,
        'R': 0.68, 'S': 0.64, 'T': 0.60, 'U': 0.72, 'V': 0.66, 'X': 0.66,
        'Y': 0.64, 'Z': 0.64
    }
    w = 0.0
    for ch in text:
        w += char_widths.get(ch, 0.58) * font_size
    return w

def generate_lockup_svg(sub_id, display_name, parent, child, category, description):
    """Generate high-contrast Apple-style standalone lockup SVG."""
    # Font sizing
    font_size = 22
    
    # Calculate widths
    if parent and child:
        w_parent = estimate_text_width(parent, font_size)
        w_sep = estimate_text_width(" • ", font_size)
        w_child = estimate_text_width(child, font_size)
        total_text_width = w_parent + w_sep + w_child
    else:
        total_text_width = estimate_text_width(display_name, font_size)

    # Symbol sizing: Height ~ 24px (1.05x cap height 22.8px)
    symbol_height = 24.0
    symbol_scale = symbol_height / 408.0  # ~0.0588
    symbol_width = 608.0 * symbol_scale  # ~35.7px
    optical_gap = 10.0
    padding_x = 16.0
    height = 46.0

    width = padding_x + symbol_width + optical_gap + total_text_width + padding_x + 4.0
    width = max(width, 140.0)

    # Baseline positioning
    baseline_y = 30.0
    symbol_y = baseline_y - symbol_height + 0.5

    # Text rendering markup
    if parent and child:
        x_parent = padding_x + symbol_width + optical_gap
        x_sep = x_parent + w_parent
        x_child = x_sep + w_sep
        text_content = f"""    <text x="{x_parent:.1f}" y="{baseline_y}" class="parent-text">{parent}</text>
    <text x="{x_sep + 3.0:.1f}" y="{baseline_y}" class="sep-text">•</text>
    <text x="{x_child:.1f}" y="{baseline_y}" class="child-text">{child}</text>"""
    else:
        x_text = padding_x + symbol_width + optical_gap
        text_content = f"""    <text x="{x_text:.1f}" y="{baseline_y}" class="parent-text">{display_name}</text>"""

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.1f} {height:.1f}" width="{width:.1f}" height="{height:.1f}" fill="none">
  <!-- cl0ud Subsystem Lockup: {display_name} -->
  <!-- Category: {category} | Description: {description} -->
  <defs>
    <linearGradient id="cyanGrad-{sub_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700&amp;display=swap');
      .parent-text {{
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: {font_size}px;
        font-weight: 600;
        fill: #F8FAFC;
        letter-spacing: -0.02em;
      }}
      .sep-text {{
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: {font_size}px;
        font-weight: 700;
        fill: #00E5FF;
      }}
      .child-text {{
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: {font_size}px;
        font-weight: 500;
        fill: #94A3B8;
        letter-spacing: -0.01em;
      }}
    </style>
  </defs>

  <!-- Container Pill -->
  <rect x="0.5" y="0.5" width="{width - 1.0:.1f}" height="{height - 1.0:.1f}" rx="8" fill="#0B0F19" stroke="#1E293B" stroke-width="1"/>

  <!-- Official Infinity-Cloud Logo Symbol -->
  <g transform="translate({padding_x:.1f}, {symbol_y:.1f}) scale({symbol_scale:.4f})" fill="url(#cyanGrad-{sub_id})">
    <path fill-rule="evenodd" d="{CLOUD_PATH}"/>
  </g>

  <!-- Typographic Subsystem Label -->
{text_content}
</svg>"""
    return svg

def generate_badge_svg(sub_id, display_name, parent, child, category, description):
    """Generate GitHub README badge matching Shields.io standards."""
    font_size = 11.0
    text_label = f"cl0ud {display_name}"
    
    # Left pill (cl0ud icon container)
    left_width = 32.0
    
    # Right pill text width
    text_width = estimate_text_width(display_name, font_size) + 18.0
    text_width = max(text_width, 48.0)
    
    total_width = left_width + text_width
    height = 24.0
    
    # Icon scaling for badge: Height = 14px
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
    <!-- Left Background: Obsidian -->
    <path fill="#0B0F19" d="M0 0 h{left_width:.1f} v{height:.1f} H0 z"/>
    <!-- Right Background: Deep Slate -->
    <path fill="#0F172A" d="M{left_width:.1f} 0 h{text_width:.1f} v{height:.1f} H{left_width:.1f} z"/>
  </g>

  <!-- Border Frame -->
  <rect x="0.5" y="0.5" width="{total_width - 1.0:.1f}" height="{height - 1.0:.1f}" rx="4" fill="none" stroke="#1E293B" stroke-width="1"/>

  <!-- Infinity Cloud Icon -->
  <g transform="translate({icon_x:.1f}, {icon_y:.1f}) scale({icon_scale:.4f})" fill="url(#badgeCyan-{sub_id})">
    <path fill-rule="evenodd" d="{CLOUD_PATH}"/>
  </g>

  <!-- Subsystem Text -->
  <text x="{text_x:.1f}" y="{text_y:.1f}" text-anchor="middle" font-family="'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="{font_size}px" font-weight="600" fill="#00E5FF" letter-spacing="-0.01em">{display_name}</text>
</svg>"""
    return svg

def main():
    root = Path(__file__).resolve().parent.parent.parent
    subsystems_dir = root / "assets" / "subsystems"
    lockups_dir = subsystems_dir / "lockups"
    badges_dir = subsystems_dir / "badges"

    lockups_dir.mkdir(parents=True, exist_ok=True)
    badges_dir.mkdir(parents=True, exist_ok=True)

    print("==================================================")
    print("cl0ud Subsystem Asset Generator")
    print(f"Total Subsystems to Process: {len(SUBSYSTEMS)}")
    print(f"Output Directory: {subsystems_dir}")
    print("==================================================")

    readme_rows = []

    for sub_id, name, parent, child, cat, desc in SUBSYSTEMS:
        lockup_filename = f"cl0ud-{sub_id}.svg"
        badge_filename = f"cl0ud-{sub_id}-badge.svg"

        lockup_path = lockups_dir / lockup_filename
        badge_path = badges_dir / badge_filename

        lockup_svg = generate_lockup_svg(sub_id, name, parent, child, cat, desc)
        badge_svg = generate_badge_svg(sub_id, name, parent, child, cat, desc)

        with open(lockup_path, "w", encoding="utf-8") as f:
            f.write(lockup_svg)

        with open(badge_path, "w", encoding="utf-8") as f:
            f.write(badge_svg)

        readme_rows.append(
            f"| `{sub_id}` | **{name}** | {cat} | ![{name}](lockups/{lockup_filename}) | ![{name}](badges/{badge_filename}) | {desc} |"
        )

    # Generate visual catalog README.md
    readme_content = f"""# cl0ud — Official Subsystem Vector Asset Registry

> **System Designation:** Standalone Subsystem Vector Assets & Lockups  
> **Brand Mark:** cl0ud Official Infinity-Cloud  
> **Typography:** Outfit (Semi-Bold 600 / Medium 500)  
> **Asset Count:** {len(SUBSYSTEMS)} Lockups + {len(SUBSYSTEMS)} Developer Badges  
> **Generator Script:** [`tools/assets/generate-subsystem-assets.py`](file:///Users/roopalisingh/Desktop/cl0ud/tools/assets/generate-subsystem-assets.py)

---

## 1. Usage in Documentation & Codebases

### Markdown Inline Lockup
```markdown
![cl0ud Bedrock](assets/subsystems/lockups/cl0ud-bedrock.svg)
![cl0ud Wireframe](assets/subsystems/lockups/cl0ud-wireframe.svg)
![cl0ud Access • Latch](assets/subsystems/lockups/cl0ud-access-latch.svg)
![cl0ud Binzo • Holonomic](assets/subsystems/lockups/cl0ud-binzo-holonomic.svg)
```

### GitHub README Shield Badge
```markdown
[![cl0ud Bedrock](assets/subsystems/badges/cl0ud-bedrock-badge.svg)](https://github.com/Ojas-sta/cl0ud-brand-engineering)
[![cl0ud Access Latch](assets/subsystems/badges/cl0ud-access-latch-badge.svg)](https://github.com/Ojas-sta/cl0ud-brand-engineering)
```

### HTML / Web Embedding
```html
<img src="/assets/subsystems/lockups/cl0ud-access-latch.svg" alt="cl0ud Access Latch" height="46" />
```

---

## 2. Master Gallery of All Subsystem Assets

| ID | Subsystem Name | Architectural Domain | Standalone Lockup Asset | Developer Badge Asset | Technical Scope |
| :--- | :--- | :--- | :--- | :--- | :--- |
""" + "\n".join(readme_rows) + """

---

## 3. Vector Specifications

- **Aspect Ratio:** Normalized $608 : 408$ master infinity-cloud icon geometry.
- **Color Finishes:**
  - Symbol: Electric Cyan gradient (`#00E5FF` $\\rightarrow$ `#38BDF8`).
  - Container: Deep Obsidian (`#0B0F19`) with `#1E293B` stroke.
  - Text: Crisp Cloud White (`#F8FAFC`), Delimiter (`#00E5FF`), Child (`#94A3B8`).
- **Typography:** Self-contained `@import` rule for Google Fonts Outfit (`600`/`500`) with system fallback.
"""

    with open(subsystems_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print(f"Generated {len(SUBSYSTEMS)} lockup SVGs in {lockups_dir}")
    print(f"Generated {len(SUBSYSTEMS)} badge SVGs in {badges_dir}")
    print(f"Generated Catalog README in {subsystems_dir / 'README.md'}")
    print("SUCCESS: All cl0ud subsystem assets generated successfully.")

if __name__ == "__main__":
    main()
