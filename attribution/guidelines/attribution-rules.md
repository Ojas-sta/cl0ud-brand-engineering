# cl0ud — Attribution Rules & Contribution Matrix

> **System Designation:** Intellectual Property & Attribution Governance  
> **Brand Mark:** cl0ud  
> **Lead Architect:** Ojas Singh  
> **Specification Reference:** [`cl0ud-brand-spec.json`](file:///Users/roopalisingh/Desktop/cl0ud/cl0ud-brand-spec.json)

---

## 1. Principles of Ethical Attribution

In engineering collaborations, intellectual honesty is paramount. Attributing a system properly ensures that:
1. Student engineers and peer innovators receive public credit for their inventions.
2. Institutional partners (e.g. DPS Indirapuram) are recognized for supporting research.
3. cl0ud’s systems architecture and engineering assistance are accurately demarcated without overreaching.

```mermaid
flowchart TD
    Task[Incoming Engineering Project] --> Assess{Level of cl0ud Involvement?}
    Assess -->|100% Internal Creation| C1[Created by cl0ud]
    Assess -->|Core Technical Architecture| C2[Engineered by cl0ud]
    Assess -->|Equal Team Capstone| C3[Co-engineered by Ojas Singh | Powered by cl0ud]
    Assess -->|Advisory / Guidance| C4[Technical Assistance by cl0ud & Ojas Singh]
    Assess -->|Tooling / Runtime Use| C5[Powered by cl0ud]
```

---

## 2. Standardized Contribution Matrix

The cl0ud brand strictly enforces eight (8) standardized contribution tiers. Use the following guide to determine the required formula:

| Tier | Attribution Formula | Usage Criteria & Authority | Example Case Study |
| :--- | :--- | :--- | :--- |
| **Tier 1** | **`Created by cl0ud`** | 100% original conception, CAD, firmware, and code authored entirely by Ojas Singh under the cl0ud banner. | *WorldXD JEPA Simulation Engine* |
| **Tier 2** | **`Engineered by cl0ud`** | Lead engineering execution across mechanical, electrical, and software domains. | *Spatial-OS Web Gesture Engine* |
| **Tier 3** | **`Co-engineered by Ojas Singh`** | Equal technical contribution within a multidisciplinary team or school capstone. | *Project CLOUD (Unitree Go2 Quadruped)* |
| **Tier 4** | **`Developed by cl0ud`** | Hands-on software, web development, or microcontroller programming for an existing project. | *DPSI Exhibition 3D Web App* |
| **Tier 5** | **`Technical assistance by cl0ud`** | Mentorship, sensor calibration math, circuit review, debugging, or tracking algorithm advice provided to external creators. | *Autonomous Mobile Smart Dustbin / Hydroponics IoT* |
| **Tier 6** | **`Powered by cl0ud`** | External project utilizes cl0ud runtime software, UI templates, or communication protocols. | *DPSI Exhibition 3D Floor Plan* |
| **Tier 7** | **`Designed by cl0ud`** | Contribution is primarily industrial enclosure styling, 3D visualization, or graphics. | *Exhibition Plinth Styling* |
| **Tier 8** | **`Collaborated with [Organization]`** | Formal partnership acknowledging institutional hosts, makerspaces, or laboratories. | *Collaborated with DPS Indirapuram* |

---

## 3. Mandatory vs. Optional Attribution

### Mandatory Contexts
Attribution is **mandatory** whenever:
- A school exhibition booth, competition presentation, or public demonstration features cl0ud CAD models, circuit designs, or software.
- A public Git repository forks, imports, or bundles cl0ud libraries or firmware maps.
- A research paper, report, or monograph reproduces cl0ud architectures or schematics.

### Permitted Variances
- In space-constrained printed labels ($\le 30\text{mm}$), the short badge `Powered by cl0ud` or `Co-engineered by Ojas Singh` may be used in place of the full combined block.
- For purely private educational experiments not shared publicly, attribution is recommended but not legally enforced.

---

## 4. Resolving Ambiguities

If unsure which attribution tier applies to a project:
1. Default to **`Technical assistance by cl0ud | Ojas Singh`** if cl0ud provided advisory guidance or reviewed code.
2. Default to **`Co-engineered by Ojas Singh`** if Ojas Singh wrote production code or built physical circuits.
3. Contact Ojas Singh at `ojasctc@gmail.com` to confirm attribution before public exhibition.
