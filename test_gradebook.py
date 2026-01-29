from unittest.mock import unittest 
from io import patch 
import StringIO
import sys

# Attempt to import the student's 'main' function
# We use a try/except block just in case the file doesn't exist or has syntax errors
try:
    from gradebook_fix import main
except ImportError:
    main = None

class TestGradebook(unittest.TestCase):

    def setUp(self):
        # redirect stdout to capture print statements
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # restore stdout so we can see test results
        sys.stdout = sys.__stdout__

    @patch('builtins.input')
    def test_gradebook_happy_path(self, mock_input):
        """
        Test 1: Standard Input
        Simulates:
        - 2 students
        - Student 1: '  alice  ', score 80 (Pass)
        - Student 2: 'bob', score 30 (Fail)
        """
        if main is None:
            self.fail("Could not import 'main' from 'gradebook_fix.py'. Check filename and syntax.")

        # inputs must match the order the program asks for them:
        # 1. Count -> "2"
        # 2. Name 1 -> "  alice  " (testing .strip())
        # 3. Score 1 -> "80"
        # 4. Name 2 -> "bob"
        # 5. Score 2 -> "30"
        mock_input.side_effect = ["2", "  alice  ", "80", "bob", "30"]

        try:
            main()
        except Exception as e:
            self.fail(f"Your code crashed with this error: {e}")

        # Get the printed output
        output = self.held_output.getvalue()

        # Checks
        self.assertIn("Alice", output, "Did not correct capitalization for 'alice' (check .title())")
        self.assertIn("Pass", output, "Did not correctly identify a Pass (Score 80)")
        self.assertIn("Fail", output, "Did not correctly identify a Fail (Score 30)")

    @patch('builtins.input')
    def test_gradebook_validation(self, mock_input):
        """
        Test 2: Validation Logic
        Simulates invalid scores to ensure the loop keeps asking.
        - 1 student
        - Name: Charlie
        - Score: -10 (Invalid)
        - Score: 105 (Invalid)
        - Score: 50 (Valid)
        """
        if main is None:
            self.fail("Could not import 'main'.")

        # Inputs: Count, Name, Bad Score, Bad Score, Good Score
        mock_input.side_effect = ["1", "Charlie", "-10", "105", "50"]

        try:
            main()
        except StopIteration:
            self.fail("Infinite Loop or Input Error: The code kept asking for input but ran out of mock values.")
        except Exception as e:
            self.fail(f"Crashed during validation test: {e}")

        output = self.held_output.getvalue()
        
        # Check if the error message appeared
        self.assertIn("Invalid", output, "The code accepts invalid scores (negative or >100) without complaining.")
        self.assertIn("Charlie", output)
        self.assertIn("Pass", output)

if __name__ == '__main__':
    print("Running tests on 'gradebook_fix.py'...\n")
    unittest.main(verbosity=2)
