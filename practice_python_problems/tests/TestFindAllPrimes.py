import unittest

from src.FindAllPrimes import FindAllPrimes


class TestFindAllPrimes(unittest.TestCase):
    def setUp(self):
        self.allPrimeNums = FindAllPrimes()
    def test_convert_char_to_cap(self):
        expected_primes = [2, 3, 5, 7]
        self.assertEqual(expected_primes, self.allPrimeNums.findAllPrimes(10))


if __name__ == "__main__":
    unittest.main()

