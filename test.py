import unittest
from unittest.mock import Mock, patch
from main import modificator, triggerException, triggerZero


class TestModificator(unittest.TestCase):
    def testmod1(self):
        self.assertEqual(modificator(1), -5)
    def testmod2(self):
        self.assertEqual(modificator(2), -4)
    def testmod3(self):
        self.assertEqual(modificator(4), -3)
    def testmod4(self):
        self.assertEqual(modificator(6), -2)
    def testmod5(self):
        self.assertEqual(modificator(8), -1)
    def testmod6(self):
        self.assertEqual(modificator(10), 0)
    def testmod7(self):
        self.assertEqual(modificator(12), 1)
    def testmod8(self):
        self.assertEqual(modificator(14), 2)
    def testmod9(self):
        self.assertEqual(modificator(18), 4)
    def testmod10(self):
        self.assertEqual(modificator(20), 5)
    def testTriggerExept1(self):
        self.assertEqual(triggerException(30),30)
    def testTriggerExept2(self):
        with self.assertRaises(Exception):
            exc = triggerException(45)
    def testTriggerZero1(self):
        self.assertRaises(triggerException(21), 21)
    def testTriggerZero2(self):
        with self.assertRaises(Exception):
            exc = triggerZero(-1)

if __name__ == "__main__":
  unittest.main()