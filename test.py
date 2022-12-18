import unittest
from main import modificator

class TestModificator(unittest.TestCase):
    def test_mod1(self):
        self.assertEqual(modificator(0), -5)
    def test_mod2(self):
        self.assertEqual(modificator(2), -4)
    def test_mod3(self):
        self.assertEqual(modificator(4), -3)
    def test_mod4(self):
        self.assertEqual(modificator(6), -2)



if __name__ == "__main__":
  unittest.main()