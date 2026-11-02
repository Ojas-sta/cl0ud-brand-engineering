#!/usr/bin/env python3
"""
cl0ud Credit Injector CLI Tool
Automates the safe, non-destructive injection of standardized cl0ud and Ojas Singh
attribution badges, README sections, code headers, and web components into target projects.
"""

import os
import sys
import argparse
from pathlib import Path

# Attribution configurations by role
ROLE_CONFIGS = {
    "co-engineered": {
        "title": "Co-engineered by Ojas Singh | Powered by cl0ud",
        "top_shield": (
            "[![Powered by cl0ud](https://img.shields.io/badge/Powered%20by-cl0ud-00E5FF"
            "?style=for-the-badge&logoColor=0B0F19&labelColor=0B0F19)]"
            "(https://github.com/Ojas-sta/cl0ud-brand-engineering)\n"
            "[![Co-engineered by Ojas Singh](https://img.shields.io/badge/Co--engineered%20by-Ojas%20Singh-1E3A8A"
            "?style=for-the-badge&logoColor=white&labelColor=0B0F19)]"
            "(https://github.com/Ojas-sta)"
        ),
        "card_badge": (
            "<div align=\"center\">\n"
            "  <a href=\"https://github.com/Ojas-sta/cl0ud-brand-engineering\">\n"
            "    <img src=\"https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/badges/cl0ud-credit-card.svg\" "
            "alt=\"Powered by cl0ud | Co-engineered by Ojas Singh\" width=\"100%\" style=\"max-width: 820px;\" />\n"
            "  </a>\n"
            "</div>"
        ),
        "section_role": "Co-engineered by",
        "involvement": "Co-engineered by Ojas Singh | Systems Architecture powered by cl0ud"
    },
    "technical-assistance": {
        "title": "Technical Assistance by cl0ud & Ojas Singh",
        "top_shield": (
            "[![Powered by cl0ud](https://img.shields.io/badge/Powered%20by-cl0ud-00E5FF"
            "?style=for-the-badge&logoColor=0B0F19&labelColor=0B0F19)]"
            "(https://github.com/Ojas-sta/cl0ud-brand-engineering)\n"
            "[![Technical Assistance](https://img.shields.io/badge/Technical%20Assistance-cl0ud%20%7C%20Ojas%20Singh-00E5FF"
            "?style=for-the-badge&labelColor=0B0F19)]"
            "(https://github.com/Ojas-sta)"
        ),
        "card_badge": (
            "<div align=\"center\">\n"
            "  <a href=\"https://github.com/Ojas-sta/cl0ud-brand-engineering\">\n"
            "    <img src=\"https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/badges/cl0ud-credit-card.svg\" "
            "alt=\"Powered by cl0ud | Technical Assistance by Ojas Singh\" width=\"100%\" style=\"max-width: 820px;\" />\n"
            "  </a>\n"
            "</div>"
        ),
        "section_role": "Technical Assistance & Advisory by",
        "involvement": "Technical Assistance provided by cl0ud & Ojas Singh"
    },
    "powered-by": {
        "title": "Powered by cl0ud",
        "top_shield": (
            "[![Powered by cl0ud](https://img.shields.io/badge/Powered%20by-cl0ud-00E5FF"
            "?style=for-the-badge&logoColor=0B0F19&labelColor=0B0F19)]"
            "(https://github.com/Ojas-sta/cl0ud-brand-engineering)"
        ),
        "card_badge": (
            "<div align=\"center\">\n"
            "  <a href=\"https://github.com/Ojas-sta/cl0ud-brand-engineering\">\n"
            "    <img src=\"https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/badges/cl0ud-credit-card.svg\" "
            "alt=\"Powered by cl0ud\" width=\"100%\" style=\"max-width: 820px;\" />\n"
            "  </a>\n"
            "</div>"
        ),
        "section_role": "Systems Architecture powered by",
        "involvement": "Powered by cl0ud Systems Architecture"
    },
    "created-by": {
        "title": "Created by cl0ud | Engineered by Ojas Singh",
        "top_shield": (
            "[![Created by cl0ud](https://img.shields.io/badge/Created%20by-cl0ud-00E5FF"
            "?style=for-the-badge&logoColor=0B0F19&labelColor=0B0F19)]"
            "(https://github.com/Ojas-sta/cl0ud-brand-engineering)\n"
            "[![Engineered by Ojas Singh](https://img.shields.io/badge/Engineered%20by-Ojas%20Singh-1E3A8A"
            "?style=for-the-badge&logoColor=white&labelColor=0B0F19)]"
            "(https://github.com/Ojas-sta)"
        ),
        "card_badge": (
            "<div align=\"center\">\n"
            "  <a href=\"https://github.com/Ojas-sta/cl0ud-brand-engineering\">\n"
            "    <img src=\"https://raw.githubusercontent.com/Ojas-sta/cl0ud-brand-engineering/main/assets/badges/cl0ud-credit-card.svg\" "
            "alt=\"Created by cl0ud | Engineered by Ojas Singh\" width=\"100%\" style=\"max-width: 820px;\" />\n"
            "  </a>\n"
            "</div>"
        ),
        "section_role": "Creator & Lead Architect:",
        "involvement": "Conceived and created under cl0ud by Ojas Singh"
    }
}

def find_readme(repo_dir: Path):
    for candidate in ["README.md", "readme.md", "README.MD"]:
        path = repo_dir / candidate
        if path.exists():
            return path
    return None

def process_readme(readme_path: Path, role: str, team: str, scope: str, institution: str, use_card: bool, dry_run: bool):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    config = ROLE_CONFIGS.get(role, ROLE_CONFIGS["co-engineered"])

    # Check if already credited
    if "cl0ud" in content and "Ojas Singh" in content:
        print(f"[SKIP] README already contains cl0ud and Ojas Singh credits: {readme_path}")
        return False

    badge_to_inject = config["card_badge"] if use_card else config["top_shield"]

    # 1. Inject badge after title or at top
    lines = content.splitlines()
    injected_lines = []
    injected_badge = False

    for i, line in enumerate(lines):
        injected_lines.append(line)
        if line.startswith("# ") and not injected_badge:
            injected_lines.append("")
            injected_lines.append(badge_to_inject)
            injected_lines.append("")
            injected_badge = True

    if not injected_badge:
        injected_lines = [badge_to_inject, ""] + injected_lines

    # 2. Build attribution section
    attribution_section = [
        "",
        "## 🤝 Engineering Attribution & Credits",
        "",
        f"- **Primary Project Authors / Team:** {team or '[Student Team / Creators]'}",
        f"- **Systems Architecture & Mechatronics:** Powered by **[cl0ud](https://github.com/Ojas-sta/cl0ud-brand-engineering)**",
        f"- **{config['section_role']}:** [Ojas Singh](https://github.com/Ojas-sta) (`ojasctc@gmail.com`)",
        f"- **Scope of Engineering:** {scope or 'Systems architecture, circuit protection & algorithms'}",
        f"- **Academic Institution / Makerspace:** {institution or 'Delhi Public School Indirapuram (DPSI)'}",
        ""
    ]

    # Find license section or append before end
    new_content_lines = []
    injected_section = False
    for line in injected_lines:
        if (line.startswith("## License") or line.startswith("## 📄 License")) and not injected_section:
            new_content_lines.extend(attribution_section)
            injected_section = True
        new_content_lines.append(line)

    if not injected_section:
        new_content_lines.extend(attribution_section)

    final_content = "\n".join(new_content_lines) + "\n"

    print(f"[{'DRY-RUN' if dry_run else 'APPLIED'}] Injected attribution into {readme_path}")
    if not dry_run:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(final_content)
    return True

def generate_code_header(file_path: Path, project_name: str, scope: str):
    ext = file_path.suffix.lower()
    if ext in [".cpp", ".h", ".hpp", ".c", ".ino"]:
        return (
            "/*\n"
            f" * Project:       {project_name}\n"
            f" * Scope:         {scope}\n"
            " * Architecture:  Powered by cl0ud (https://github.com/Ojas-sta/cl0ud-brand-engineering)\n"
            " * Co-Engineered: Ojas Singh <ojasctc@gmail.com>\n"
            " */\n\n"
        )
    elif ext in [".py", ".sh"]:
        return (
            "# ==============================================================================\n"
            f"# Project:       {project_name}\n"
            f"# Scope:         {scope}\n"
            "# Architecture:  Powered by cl0ud (https://github.com/Ojas-sta/cl0ud-brand-engineering)\n"
            "# Co-Engineered: Ojas Singh <ojasctc@gmail.com>\n"
            "# ==============================================================================\n\n"
        )
    return None

def main():
    parser = argparse.ArgumentParser(description="cl0ud Credit Injector CLI Tool")
    parser.add_argument("--repo", default=".", help="Path to target project repository")
    parser.add_argument("--role", choices=["co-engineered", "technical-assistance", "powered-by", "created-by"], default="co-engineered", help="Attribution tier")
    parser.add_argument("--team", default="", help="Name of collaborating team or creators")
    parser.add_argument("--scope", default="", help="Scope of technical contribution")
    parser.add_argument("--institution", default="Delhi Public School Indirapuram (DPSI)", help="Host institution")
    parser.add_argument("--card", action="store_true", help="Embed full credit card instead of shield badges")
    parser.add_argument("--dry-run", action="store_true", help="Simulate changes without modifying files")
    parser.add_argument("--apply", action="store_true", help="Apply changes directly to files")

    args = parser.parse_args()

    if not args.dry_run and not args.apply:
        print("Please specify either --dry-run (preview) or --apply (write changes).")
        sys.exit(1)

    repo_dir = Path(args.repo).resolve()
    print(f"Scanning target repository: {repo_dir}")
    print(f"Attribution Role: {args.role}")

    readme = find_readme(repo_dir)
    if readme:
        process_readme(readme, args.role, args.team, args.scope, args.institution, args.card, args.dry_run)
    else:
        print(f"[WARN] No README.md found in {repo_dir}")

    print("\nCredit injection process complete.")

if __name__ == "__main__":
    main()
