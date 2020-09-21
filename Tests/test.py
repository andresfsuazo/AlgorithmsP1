import unittest
from Andres import *

"""Unit Tests for entire application. Should be divided into separate files later"""

class PrimeTest(unittest.TestCase):

    def setUp(self):
        self.k = 30

    def test_180_isPrime(self):
        print("Test on composite number...")
        self.assertFalse(isPrime(180, self.k))

    def test_7_isPrime(self):
        print("Test on prime number...")
        self.assertTrue(isPrime(7, self.k))

    def test_negative_isPrime(self):
        print("Test on negative number...")
        self.assertFalse(isPrime(-7, self.k))

    def test_zero_isPrime(self):
        print("Test on zero...")
        self.assertFalse(isPrime(0, self.k))

class PrimeGenerationTest(unittest.TestCase):

    def setUp(self):
        self.k = 30

    def test_whole_randomPrime(self):
        print("Test on whole number...")
        result = randomPrime(1, 100)
        self.assertTrue(isPrime(result, self.k))

    def test_integers_randomPrime(self):
        print("Test on integers...")
        with self.assertRaises(ValueError):
            randomPrime(-4, 15)

    def test_inverted_randomPrime(self):
        print("Test on min/max inverted...")
        with self.assertRaises(ValueError):
            randomPrime(100, 10)

if __name__ == '__main__':
    unittest.main()