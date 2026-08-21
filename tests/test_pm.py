import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "pm.py"
SPEC = importlib.util.spec_from_file_location("pm", MODULE_PATH)
assert SPEC and SPEC.loader
PM = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PM)


class ProjectManagementDoctorTest(unittest.TestCase):
    def test_example_config_has_exact_required_keys(self) -> None:
        self.assertEqual(set(PM.load_project()), PM.REQUIRED_PROJECT_KEYS)

    def test_doctor_passes_for_template(self) -> None:
        self.assertEqual(PM.doctor(), 0)


if __name__ == "__main__":
    unittest.main()
