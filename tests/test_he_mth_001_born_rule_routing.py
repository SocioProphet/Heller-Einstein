from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "methodology" / "born-rule-interface-routing.md"
REGISTRY = ROOT / "docs" / "identifier-reservations.md"


class TestHEMTH001BornRuleRouting(unittest.TestCase):
    def test_doc_exists_and_routes_three_repos(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "Born Rule Interface Routing",
            "Heller-Einstein",
            "Heller-Dirac",
            "Yang-Mills",
            "HE-PROJ-001",
            "Markov kernel",
            "P(m) = Tr(E_m rho)",
            "interface-induced trace kernel",
            "positive Hilbert-space state/effect pairing",
        ]:
            self.assertIn(token, text)

    def test_non_claim_boundary_is_explicit(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "does not derive the Born rule",
            "does not derive quantum mechanics",
            "does not derive noncommuting observables or entanglement",
            "does not prove that Born probabilities are projection-induced Markov kernels",
            "does not identify a physical latent state space for quantum theory",
            "does not transfer proof content into any Clay-program repository",
        ]:
            self.assertIn(token, text)

    def test_registry_activates_he_mth_001(self) -> None:
        text = REGISTRY.read_text(encoding="utf-8")
        self.assertIn("`HE-MTH-001` | Born-rule interface routing across Heller-Einstein, Heller-Dirac, and Yang-Mills | `docs/methodology/born-rule-interface-routing.md`", text)
        self.assertIn("`HE-MTH-001` | Born-rule interface routing across Heller-Einstein, Heller-Dirac, and Yang-Mills | active", text)
        self.assertIn("`HE-MTH-002` | Structural-cognate map to Heller-Dirac `HD-*` identifiers | reserved", text)


if __name__ == "__main__":
    unittest.main()
