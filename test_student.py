
import unittest
from student import validate_student_email


class TestStudentEmail(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(
            validate_student_email("student@example.com")
        )

    def test_invalid_email(self):
        self.assertFalse(
            validate_student_email("studentexample.com")
        )


if __name__ == "__main__":
    unittest.main()
