# cl0ud — Git Commit Conventions & Versioning

> **System Designation:** Technical Standards — Git Repository Governance  
> **Standard:** Conventional Commits v1.0.0 & Semantic Versioning (SemVer 2.0.0)  
> **Brand Mark:** cl0ud  
> **Specification Reference:** [`cl0ud-brand-spec.json`](file:///Users/roopalisingh/Desktop/cl0ud/cl0ud-brand-spec.json)

---

## 1. Commit Message Structure

Every commit within a cl0ud-maintained or co-engineered repository must follow the Conventional Commits specification:

```text
<type>(<scope>): <short description in imperative mood>

[optional body explaining technical motivation and physics/circuits impacted]

[optional footer referencing issue numbers, breaking changes, or attribution]
```

### Allowed Types
- **`feat`**: A new feature, sensor driver, or architectural module.
- **`fix`**: A bug fix in software, wiring schematic correction, or kinematic patch.
- **`docs`**: Documentation updates, monographs, or README revisions.
- **`style`**: Code formatting, whitespace, or visual token alignment.
- **`refactor`**: Code restructuring without changing behavior or kinematics.
- **`perf`**: Optimizations reducing render latency, bus bandwidth, or compute cycles.
- **`test`**: Adding unit tests, simulation test cases, or hardware verification routines.
- **`chore`**: Maintenance, build configs, dependencies, or tool updates.
- **`legal`**: Updates to Terms & Conditions, licenses, or attribution policies.

### Example Commits
```text
feat(mechatronics): add silicone vibration dampener CAD specs for D435i mount

fix(power): add inductive back-EMF flyback diode on 12V buck regulator line

docs(monograph): release rev 5.0.0 master architectural specification for CLOUD
```

---

## 2. Semantic Versioning (SemVer 2.0.0)

Repository releases follow `MAJOR.MINOR.PATCH`:
- **MAJOR:** Breaking hardware wiring changes, incompatible API endpoints, or brand redesigns.
- **MINOR:** Backwards-compatible new features, added project entries, or new CAD components.
- **PATCH:** Bug fixes, typo corrections, or minor calibration adjustments.
