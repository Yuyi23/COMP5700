import unittest
import Fizzbuzz.fizzbuzz as fb

class fizzBuzzText(unittest.TestCase):
    
# Analysis
#    fizzbuzz(n)
#
#    inputs:
#        n:    integer, (0, 50], mandatory, unvalidated
#
#    outputs:
#        side-effects:  no state change
#        returns:  string, one of the following:
#                {"fizz", "buzz", "fizzbuzz", str(n), "Danger, Will Robinson"}
#    confidence level:  BVA
#
# Happy path
#     test 010:    nominal value of n that is evenly divisible by 3 only:  3
#                 result:  "fizz"
#    test 020:    nominal value of n that is evenly divisible by 5 only:  25
#                 result:  "buzz"
#    test 030:    nominal value of n this evenly divisible by 3 and 5:  45
#                result:  "fizzbuzz"
#    test 040:    nominal value of n that is not evenly div by 3 or 5:  23
#                result:  "23"
#    test 050:    low bound of n:  1
#                result:  "1"
#    test 060:    high bound of n:  50
#                result: "buzz"
#
# Sad path
#    test 910:    non-integer value of n:  3.3
#                result "Danger, Will Robinson"
#    test 920:    missing n
#                result
#    test 930:    less than low bound:  0
#                result
#    test 940:    greater than high bound:  51
#                result
#
# Happy Path tests
    def test010_ShouldTestNominalNEvenlyDivisibleBy3(self):
        n = 3
        expectedResult = "fizz"
        actualResult = fb.fizzbuzz(n)
        self.assertEqual(expectedResult, actualResult)
        
    def test020_ShouldTestNominalNEvenlyDivisibleBy5(self):
        n = 25
        expectedResult = "buzz"
        actualResult = fb.fizzbuzz(n)
        self.assertEqual(expectedResult, actualResult)

    def test030_ShouldTestNominalNEvenlyDivisibleBy3And5(self):
        n = 45
        expectedResult = "fizzbuzz"
        actualResult = fb.fizzbuzz(n)
        self.assertEqual(expectedResult, actualResult)

    def test040_ShouldTestNominalNNotEvenlyDivisibleBy3Or5(self):
        n = 2
        expectedResult = "2"
        actualResult = fb.fizzbuzz(n)
        self.assertEqual(expectedResult, actualResult)
        
    def test050_ShouldTestLowBoundN(self):
        n = 1
        expectedResult = "1"
        actualResult = fb.fizzbuzz(n)
        self.assertEqual(expectedResult, actualResult)
        
    def test060_ShouldTestHighBoundN(self):
        n = 50
        expectedResult = "buzz"
        actualResult = fb.fizzbuzz(n)
        self.assertEqual(expectedResult, actualResult)
        
# Sad Paths
    def test910_ShouldTestNonIntegerN(self):
        n = 3.3
        expectedResult = "Danger, Will Robinson"
        actualResult = fb.fizzbuzz(n)
        self.assertEqual(expectedResult, actualResult)    
        
    def test920_ShouldTestMissiN(self):
        expectedResult = "Danger, Will Robinson"
        actualResult = fb.fizzbuzz()
        self.assertEqual(expectedResult, actualResult)     

    def test930_ShouldTestLessThanLowBound(self):
        n = 0
        expectedResult = "Danger, Will Robinson"
        actualResult = fb.fizzbuzz(n)
        self.assertEqual(expectedResult, actualResult) 
        
    def test940_ShouldTestGreaterThanHighBound(self):
        n = 51
        expectedResult = "Danger, Will Robinson"
        actualResult = fb.fizzbuzz(n)
        self.assertEqual(expectedResult, actualResult) 
