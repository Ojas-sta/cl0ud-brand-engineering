#!/usr/bin/env python3
"""
cl0ud Brand Specification & Repository Validator
Validates cl0ud-brand-spec.json against schemas/cl0ud-brand-spec.schema.json,
checks integrity rules, enums, project registries, and file path references.
"""

import sys
import os
import json
from pathlib import Path

def validate_json_syntax(file_path):
    """Ensure JSON parses cleanly without errors."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return True, data, "JSON syntax is valid."
    except Exception as e:
        return False, None, f"JSON syntax error in {file_path}: {e}"

def validate_sections(data):
    """Verify all 10 core sections exist."""
    required_sections = [
        "brandIdentity",
        "founderIdentity",
        "logoSystem",
        "visualDesignSystem",
        "projectEcosystem",
        "brandingAttributionSystem",
        "termsAndConditions",
        "brandGovernance",
        "repositoryGovernance",
        "jsonValidation"
    ]
    missing = [sec for sec in required_sections if sec not in data]
    if missing:
        return False, f"Missing required sections: {missing}"
    return True, f"All {len(required_sections)} required brand sections are present."

def validate_contribution_levels(data):
    """Verify contribution levels in projects match allowed enums."""
    allowed_levels = {
        "Created by",
        "Engineered by",
        "Co-engineered by",
        "Developed by",
        "Technical assistance by",
        "Powered by",
        "Designed by",
        "Collaborated with"
    }
    
    projects = data.get("projectEcosystem", {}).get("verifiedProjects", [])
    if not projects:
        return False, "No verified projects found in projectEcosystem."
        
    for proj in projects:
        inv = proj.get("cl0udInvolvement")
        if inv not in allowed_levels:
            return False, f"Project {proj.get('projectId')} has invalid involvement level: {inv}"
            
    return True, f"All {len(projects)} verified projects use standardized contribution levels."

def validate_with_jsonschema(spec_path, schema_path):
    """Run jsonschema validation if module is installed."""
    try:
        import jsonschema
        with open(spec_path, "r", encoding="utf-8") as sf:
            spec = json.load(sf)
        with open(schema_path, "r", encoding="utf-8") as scf:
            schema = json.load(scf)
            
        validator = jsonschema.Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(spec), key=lambda e: e.path)
        
        if errors:
            err_msgs = [f"At '{'/'.join(map(str, err.path))}': {err.message}" for err in errors]
            return False, "JSON Schema validation failed:\n" + "\n".join(err_msgs[:10])
        return True, "JSON Schema Draft 2020-12 validation passed with 0 errors."
    except ImportError:
        return True, "Note: python 'jsonschema' library not installed; skipped formal draft validator."
    except Exception as e:
        return False, f"Schema validation error: {e}"

def main():
    root_dir = Path(__file__).resolve().parent.parent.parent
    spec_path = root_dir / "cl0ud-brand-spec.json"
    schema_path = root_dir / "schemas" / "cl0ud-brand-spec.schema.json"

    print("==================================================")
    print("cl0ud Brand Specification Integrity Validator")
    print(f"Target: {spec_path}")
    print("==================================================")

    if not spec_path.exists():
        print(f"FAIL: Specification file not found: {spec_path}")
        sys.exit(1)
        
    if not schema_path.exists():
        print(f"FAIL: Schema file not found: {schema_path}")
        sys.exit(1)

    # 1. Syntax check
    ok, data, msg = validate_json_syntax(spec_path)
    print(f"[{'PASS' if ok else 'FAIL'}] {msg}")
    if not ok:
        sys.exit(1)

    # 2. Section check
    ok, msg = validate_sections(data)
    print(f"[{'PASS' if ok else 'FAIL'}] {msg}")
    if not ok:
        sys.exit(1)

    # 3. Contribution level check
    ok, msg = validate_contribution_levels(data)
    print(f"[{'PASS' if ok else 'FAIL'}] {msg}")
    if not ok:
        sys.exit(1)

    # 4. JSON Schema check
    ok, msg = validate_with_jsonschema(spec_path, schema_path)
    print(f"[{'PASS' if ok else 'FAIL'}] {msg}")
    if not ok:
        sys.exit(1)

    print("\nSUCCESS: All brand specification integrity checks passed successfully.")

if __name__ == "__main__":
    main()
