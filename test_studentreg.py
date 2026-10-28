
import unittest
from studentreg import register_student


class TestStudentRegistration(unittest.TestCase):

    def test_valid_student(self):
        result = register_student("Anu Mali", "anu@example.com", "24")
        self.assertEqual(result, "Student registered successfully")

    def test_invalid_name(self):
        result = register_student("", "anu@example.com", "24")
        self.assertEqual(result, "Invalid: Name is required")

    def test_invalid_email(self):
        result = register_student("Anu Mali", "anu-example.com", "24")
        self.assertEqual(result, "Invalid: Email address")

    def test_invalid_roll_number(self):
        result = register_student("Anu Mali", "anu@example.com", "")
        self.assertEqual(result, "Invalid: Roll number is required")


if __name__ == "__main__":
    unittest.main()
