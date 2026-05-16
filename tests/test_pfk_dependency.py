from pathlib import Path
import os
import unittest


ROOT = Path(__file__).resolve().parents[1]
HELLER_GODEL_COMMIT = "988307215ad38ccb16514311222184a1b757752b"
HELLER_DIRAC_COMMIT = "e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993"
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
    "HE-INT-",
    "HE-PROJ-",
    "HE-PHYS-",
    "HE-PLC-",
    "HE-EX-",
    "HE-MTH-",
    "A-HE-",
]


class TestHellerEinsteinBootstrap(unittest.TestCase):
    def test_dependencies_file_exists_and_pins_upstreams(self) -> None:
        text = (ROOT / "DEPENDENCIES.md").read_text(encoding="utf-8")
        self.assertIn(HELLER_GODEL_COMMIT, text)
        self.assertIn(HELLER_DIRAC_COMMIT, text)
        self.assertIn("HG-MTH-005", text)
        self.assertIn("PFK-SCHEMA-001", text)
        self.assertIn("A-PFK-SCHEMA-001", text)
        self.assertIn("HD-FND-007", text)
        self.assertIn("HD-FND-008", text)
        self.assertIn("A-HD-TM-001", text)

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

    def test_heller_dirac_paths_resolve_when_available(self) -> None:
        hd_root_value = os.environ.get("HELLER_DIRAC_ROOT")
        if not hd_root_value:
            self.skipTest("HELLER_DIRAC_ROOT not set; dependency-resolution check runs in workflow")
        hd_root = Path(hd_root_value)
        for rel in [
            "docs/foundations/HD-FND-007-modular-operator.md",
            "docs/foundations/HD-FND-008-kms.md",
            "docs/anti-seed-dirac.md",
        ]:
            self.assertTrue((hd_root / rel).exists(), f"missing Heller-Dirac path: {rel}")

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

    def test_identifier_reservations_exist_and_namespace_clean(self) -> None:
        path = ROOT / "docs" / "identifier-reservations.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        for prefix in REQUIRED_PREFIXES:
            self.assertIn(prefix, text)
        self.assertIn("HE-INT-001", text)
        self.assertIn("HE-PROJ-001", text)
        self.assertIn("HE-PROJ-002", text)
        self.assertIn("HE-EX-001", text)
        self.assertIn("HE-EX-002", text)
        self.assertIn("HE-PROJ-INV-001", text)
        self.assertIn("HE-PROJ-TASK-001", text)
        self.assertIn("HE-FND-* — withdrawn", text)
        self.assertNotIn("| `HE-FND-001`", text)

    def test_interface_ontology_exists(self) -> None:
        path = ROOT / "docs" / "interface" / "HE-INT-001-interface-ontology.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("trace map", text)
        self.assertIn("semantic lift", text)
        self.assertIn("F_y := tau_O^{-1}(y)", text)
        self.assertIn("HE-FND-* is withdrawn", text)

    def test_projection_theorem_and_fixtures_exist(self) -> None:
        theorem = ROOT / "docs" / "projection" / "HE-PROJ-001-projection-induced-stochasticity.md"
        ex1 = ROOT / "docs" / "examples" / "HE-EX-001-discrete-phase-cycle.md"
        ex2 = ROOT / "docs" / "examples" / "HE-EX-002-continuous-phase-flow.md"
        for path in [theorem, ex1, ex2]:
            self.assertTrue(path.exists(), f"missing HE projection artifact: {path}")
        theorem_text = theorem.read_text(encoding="utf-8")
        self.assertIn("Parent interface ontology: `HE-INT-001`", theorem_text)
        self.assertIn("Markov kernel", theorem_text)
        self.assertIn("does not derive quantum mechanics", theorem_text)
        self.assertIn("HE-PROJ-INV-001", theorem_text)
        self.assertIn("Temporal Mechanics v0.24.1", theorem_text)
        self.assertIn("[[2/3, 1/3], [1/3, 2/3]]", ex1.read_text(encoding="utf-8"))
        self.assertIn("[[2/3, 1/3], [1/3, 2/3]]", ex2.read_text(encoding="utf-8"))

    def test_sufficiency_hierarchy_exists(self) -> None:
        path = ROOT / "docs" / "projection" / "HE-PROJ-002-sufficiency-hierarchy.md"
        self.assertTrue(path.exists(), "HE-PROJ-002 sufficiency hierarchy missing")
        text = path.read_text(encoding="utf-8")
        self.assertIn("HE-PROJ-002", text)
        self.assertIn("microstate sufficiency implies semantic sufficiency", text)
        self.assertIn("Converse failure: HE-EX-001 counterexample", text)
        self.assertIn("Rate-distortion framing", text)
        self.assertIn("HE-PROJ-TASK-001", text)
        self.assertIn("does not derive quantum mechanics", text)

    def test_provenance_records_exist(self) -> None:
        v17 = ROOT / "docs" / "provenance" / "einstein-heller-v1_7.md"
        tm = ROOT / "docs" / "provenance" / "temporal-mechanics-v0_24_1.md"
        for path in [v17, tm]:
            self.assertTrue(path.exists())
        self.assertIn("rendered-artifact reconstruction", v17.read_text(encoding="utf-8"))
        self.assertIn("Temporal Mechanics", tm.read_text(encoding="utf-8"))

    def test_license_exists(self) -> None:
        path = ROOT / "LICENSE"
        self.assertTrue(path.exists())
        self.assertIn("MIT License", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
