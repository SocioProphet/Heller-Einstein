from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
TM_0241 = ROOT / "docs" / "provenance" / "temporal-mechanics-v0_24_1.md"
TM_0242 = ROOT / "docs" / "provenance" / "temporal-mechanics-v0_24_2.md"


class TestTemporalMechanicsProvenance(unittest.TestCase):
    def test_both_provenance_files_exist(self) -> None:
        self.assertTrue(TM_0241.exists())
        self.assertTrue(TM_0242.exists())

    def test_v0242_references_v0241_as_successor_parent(self) -> None:
        text = TM_0242.read_text(encoding="utf-8")
        self.assertIn("Successor to: `docs/provenance/temporal-mechanics-v0_24_1.md`", text)
        self.assertIn("additive update to v0.24.1", text)

    def test_v0242_lists_new_sections(self) -> None:
        text = TM_0242.read_text(encoding="utf-8")
        for token in [
            "Section 5.5 — Quasicrystalline shell refinements",
            "Section 7.5 — Wave archetypes as projection signatures",
            "Section 12.5 — Holographic envelope as projection/preimage stress test",
            "Section 12.7 — Borel-side framework parallel and four-corner closure",
        ]:
            self.assertIn(token, text)

    def test_v0242_status_and_no_active_identifier_modification(self) -> None:
        text = TM_0242.read_text(encoding="utf-8")
        self.assertIn("bibliographic manuscript reference", text)
        self.assertIn("does not promote any new in-repo identifier", text)
        self.assertNotRegex(text, re.compile(r"HE-PROJ-001\s+(is|was|will be)\s+modified", re.IGNORECASE))

    def test_forbidden_tokens_only_appear_as_non_claims(self) -> None:
        text = TM_0242.read_text(encoding="utf-8")
        boundary = text.split("## Boundary", 1)[1]
        for token in ["theorem-grade", "Clay-direction", "continuum construction"]:
            if token in text:
                self.assertIn(token, boundary)


if __name__ == "__main__":
    unittest.main()
