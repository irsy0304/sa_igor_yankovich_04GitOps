import unittest
import python_string

class TestProgram(unittest.TestCase):
    def test_new_string(self):
        a = "a"
        b = "b"
        c = "c"
        expected_result = "abc"
        new_string = python_string.concatenate_strings(a, b, c)
        self.assertEqual(new_string, expected_result)

if __name__ == '__main__':
    unittest.main()
