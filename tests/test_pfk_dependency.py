from pathlib import Path
import os
import unittest


ROOT = Path(__file__).resolve().parents[1]
HELLER_GODEL_COMMIT = "988307215ad38ccb16514311222184a1b757752b"
CANONICAL_SCHEMA_NAMES = {
    "claim_ledger_row.schema.json",
    "event_ir.schema.json",
    "proof_artifact.schema.json",
    "calibration_bundle.schema.json",
}
REQUIRED_A_HE = [
    "A-HE-FND-001",
    "A-HE-INT-001",
    "A-HE-INT-002",
    "A-HE-PROJ-001",
    "A-HE-PROJ-002",
    "A-HE-PHYS-001",
    "A-HE-PHYS-002",
    "A-HE-PHYS-003",
    "A-HE-PLC-001",
    "A-HE-EX-001",
    "A-HE-MTH-001",
]
REQUIRED_PREFIXES = [
    "HE-FND-",
    "HE-INT-",
    "HE-PROJ-",
    "HE-PHYS-",
    "HE-PLC-",
    "HE-EX-",
    "HE-MTH-",
    "A-HE-",
]


class TestHellerEinsteinBootstrap(unittest.TestCase):
    def test_dependencies_file_exists_and_pins_heller_godel(self) -> None:
        text = (ROOT / "DEPENDENCIES.md").read_text(encoding="utf-8")
        self.assertIn(HELLER_GODEL_COMMIT, text)
        self.assertIn("HG-MTH-005", text)
        self.assertIn("PFK-SCHEMA-001", text)
        self.assertIn("A-PFK-SCHEMA-001", text)

    def test_no_local_canonical_schema_shadowing(self) -> None:
        local_schemas = ROOT / "schemas"
        if not local_schemas.exists():
            return
        local_names = {path.name for path in local_schemas.rglob("*.json")}
        shadowed = sorted(local_names & CANONICAL_SCHEMA_NAMES)
        self.assertFalse(shadowed, f"local schemas shadow canonical PFK schemas: {shadowed}")

    def test_canonical_pfk_paths_resolve_when_available(self) -> None:
        hg_root_value = os.environ.get("HELLER_GODEL_ROOT")
        if not hg_root_value:
            self.skipTest("HELLER_GODEL_ROOT not set; dependency-resolution check runs in workflow")
        hg_root = Path(hg_root_value)
        for name in CANONICAL_SCHEMA_NAMES:
            schema_path = hg_root / "proof_fabric_kernel" / "schemas" / name
            self.assertTrue(schema_path.exists(), f"missing canonical PFK schema: {name}")

    def test_scope_doc_exists(self) -> None:
        path = ROOT / "docs" / "scope.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("Typed Interface Ontology", text)
        self.assertIn("Projection-Induced Stochasticity", text)
        self.assertIn("Einstein-Cartan-Dirac", text)

    def test_anti_seed_doc_exists_and_has_required_entries(self) -> None:
        path = ROOT / "docs" / "anti-seed-einstein.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        for entry in REQUIRED_A_HE:
            self.assertIn(entry, text)

    def test_identifier_reservations_exist(self) -> None:
        path = ROOT / "docs" / "identifier-reservations.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        for prefix in REQUIRED_PREFIXES:
            self.assertIn(prefix, text)

    def test_provenance_record_exists(self) -> None:
        path = ROOT / "docs" / "provenance" / "einstein-heller-v1_7.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("rendered-artifact reconstruction", text)
        self.assertIn("provenance-only", text)

    def test_license_exists(self) -> None:
        path = ROOT / "LICENSE"
        self.assertTrue(path.exists())
        self.assertIn("MIT License", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
