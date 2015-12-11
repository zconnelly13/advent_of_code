"""
Test that all of the solutions still work and are correct
"""

from cStringIO import StringIO
from nose_parameterized import parameterized
import sys
import unittest

SOLUTIONS = {
    (1, 1): 138,
    (1, 2): 1771}


class TestSolutions(unittest.TestCase):
    """Test Solutions to each day_*_part_[1,2]"""
    number_of_problems = len(SOLUTIONS.keys()) + 1

    @parameterized.expand([(i,) for i in SOLUTIONS.iterkeys()])
    def test_problem(self, problem):
        """Test each problem

        For each problem import the module, capture the stdout
        and compare it to SOLUTIONS
        """
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        __import__("problems.day_%s_part_%s" % problem)
        sys.stdout = old_stdout
        solution = int(mystdout.getvalue())
        self.assertEqual(SOLUTIONS[problem], solution)

if __name__ == '__main__':
    unittest.main()
