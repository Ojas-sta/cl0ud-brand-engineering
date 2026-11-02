# Contributing to the cl0ud Ecosystem

Thank you for your interest in contributing to the **cl0ud** engineering brand, open mechatronics, and documentation ecosystem.

---

## 1. Code of Conduct
All contributors are expected to uphold the [Contributor Covenant](CODE_OF_CONDUCT.md) standards of respect, inclusion, and professional integrity.

---

## 2. Core Contribution Rules

1. **Never Obscure Peer Authorship:** If contributing code or CAD designs from a team project, you must explicitly document all peer authors in the metadata.
2. **Conventional Commits:** All Git commit messages must follow the [Conventional Commits](engineering/standards/commit-conventions.md) specification (`feat:`, `fix:`, `docs:`, etc.).
3. **Specification Validation:** If modifying `cl0ud-brand-spec.json`, you must run the validator before submitting your Pull Request:
   ```bash
   python3 tools/validation/validate-brand-spec.py
   ```
4. **No Broken Links:** Ensure all markdown references use valid relative paths or verified URLs.

---

## 3. Pull Request Process

1. Fork or branch from `main` (branch name format: `feat/<feature-name>` or `fix/<fix-name>`).
2. Implement your changes following [cl0ud Coding Standards](engineering/standards/coding-standards.md).
3. Validate JSON schemas and documentation integrity.
4. Submit a Pull Request targeting `main` with a clear description of the engineering rationale.
5. The Brand Administrator (Ojas Singh) will review and merge upon verification.
