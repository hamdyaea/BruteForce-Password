# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
import unittest
from BruteForce import find_password


class DemoTests(unittest.TestCase):
    def test_leading_zero_is_enumerated(self):
        self.assertEqual(find_password("00", "01"), ("00", 3))

    def test_empty(self):
        self.assertEqual(find_password("", "01"), ("", 0))

    def test_limit(self):
        self.assertEqual(find_password("111", "01", 4), (None, 4))

    def test_all_small_candidates(self):
        for target in ("0", "1", "00", "01", "10", "11"):
            self.assertEqual(find_password(target, "01")[0], target)

    def test_invalid_arguments(self):
        for args in [("2", "01", 10), ("0", "", 10), ("0", "00", 10),
                     ("0", "01", 0), ("0", "01", 1000001)]:
            with self.assertRaises(ValueError):
                find_password(*args)


if __name__ == "__main__":
    unittest.main()
