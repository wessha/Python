# import the python testing framework
import unittest
# our "unit"
# this is what we are running our test on
def isEven(n):
    if n % 2 == 0:
       return True
    else:
       return False
# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase
class IsEvenTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testTwo(self):
        self.assertEqual(isEven(2), True)
        self.assertTrue(isEven(2))
    def testThree(self):
        self.assertEqual(isEven(3), False)
        self.assertFalse(isEven(3))
    # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests

import unittest
def isOdd(n):
    if n % 2 != 0:
        return True
    else:
        return False
class IsOddTest(unittest.TestCase):

    def testOne(self):
        self.assertEqual(isOdd(3), True)
    def testFour(self):
        self.assertEqual(isOdd(4), False)
    def testFive(self):
        self.assertEqual(isOdd(5), True)
    def setUp(self) -> None:
        return super().setUp()
    def tearDown(self) -> None:
        return super().tearDown()
if __name__ == '__main__':
    unittest.main()

