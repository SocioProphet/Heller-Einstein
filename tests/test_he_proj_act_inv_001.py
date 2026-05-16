from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "projection" / "HE-PROJ-ACT-INV-001-mode-composition-law.md"
REGISTRY = ROOT / "docs" / "identifier-reservations.md"
ANTI_SEED = ROOT / "docs" / "anti-seed-einstein.md"


class TestHEProjActInv001(unittest.TestCase):
    def test_mode_composition_law_exists_and_is_conditional(self) -> None:
        self.assertTrue(DOC.exists(), "HE-PROJ-ACT-INV-001 mode-composition law missing")
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HE-PROJ-ACT-INV-001", text)
        self.assertIn("Mode-Composition Law v0.1", text)
        self.assertIn("modeling-choice-grade", text)
        self.assertIn("conditional on HE-PROJ-ACT-INV-001 mode-composition law v0.1", text)
        self.assertIn("not a theorem derived from `HE-PROJ-ACT-001` or `HE-PROJ-ACT-002`", text)
        self.assertIn("Alternative truncation, aliasing, folding, or parent-pattern conventions", text)

    def test_distinguishes_transfer_ceiling_from_lipschitz_ceiling(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("Ceiling_T(Theta)", text)
        self.assertIn("C_Lip(Theta)", text)
        self.assertIn("The two objects are distinct and must not be collapsed", text)
        self.assertIn("AdmNet(Theta) := [ C_Lip(Theta) < 1 ]", text)

    def test_v01_threshold_theorem_and_converse_boundary_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("Theorem — v0.1 thresholded reachability characterization", text)
        self.assertIn("B_eff^nz(epsilon; M,d,S_0)", text)
        self.assertIn("S_0 · HProd_epsilon · WProd_adm^nz(kappa)", text)
        self.assertIn("load-bearing independence property", text)
        self.assertIn("multi-index intermodulation", text)
        self.assertIn("specific to v0.1", text)

    def test_aliasing_fixture_really_separates_from_cutoff(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("Fixture C — aliasing genuinely separates from cutoff", text)
        self.assertIn("r = n_1 w_1 m_0 = 5 * 1 * 3 = 15", text)
        self.assertIn("hard cutoff: route dropped", text)
        self.assertIn("modular aliasing: route reaches mode 7", text)
        self.assertIn("alias_8(15) = 7", text)

    def test_prime_modulus_nonclaim_is_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("prime-modulus corollary", text)
        self.assertIn("not a statement about prime numbers", text)
        self.assertIn("prime gaps", text)
        self.assertIn("Heller-Winters prime program", text)

    def test_registry_activates_conditional_capsule_without_closing_frontier(self) -> None:
        text = REGISTRY.read_text(encoding="utf-8")
        self.assertIn("HE-PROJ-ACT-INV-001", text)
        self.assertIn("active conditional v0.1; frontier open", text)
        self.assertIn("docs/projection/HE-PROJ-ACT-INV-001-mode-composition-law.md", text)

    def test_anti_seed_enforces_conditionality(self) -> None:
        text = ANTI_SEED.read_text(encoding="utf-8")
        self.assertIn("A-HE-PROJ-ACT-INV-001", text)
        self.assertIn("v0.1 routing law is not canonical spectral attainability", text)
        self.assertIn("conditional on HE-PROJ-ACT-INV-001 mode-composition law v0.1", text)
        self.assertIn("convention-invariance theorem", text)
        self.assertIn("prime-sequence representation", text)


if __name__ == "__main__":
    unittest.main()
