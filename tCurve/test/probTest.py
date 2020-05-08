from unittest import TestCase
from tCurve.prob import prob as prob
from tCurve.prob import _integrate as _integrate
from tCurve.prob import _f as _f
import json


class ProbTest(TestCase):

    def setUp(self):
        self.nominalN = 4
        self.nominalT = 1.4398
        self.nominalTails = 1
        self.inputDictionary = {}
        self.errorValue = "error:"
        self.errorKey = "error"
        self.solutionKey = "probability"
        
    def tearDown(self):
        self.inputDictionary = {}

    def setT(self, t):
        self.inputDictionary["t"] = t

    def setN(self, n):
        self.inputDictionary["n"] = n

    def setTails(self, tails):
        self.inputDictionary["tails"] = tails
        
    def setExtra(self, extra):
        self.inputDictionary["extra"] = extra

    # 100 prob
    #    Desired level of confidence:    boundary value analysis
    #    Input-output Analysis
    #        inputs:        n -> integer, .GE.3, mandatory, unvalidated
    #                       t ->    float > 0.0, mandatory, unvalidated
    #                       tails -> integer, 1 or 2, optional, defaults to 1
    #        outputs:    float .GT. 0 .LE. 1.0
    #    Happy path analysis:
    #       n:       nominal value    n=6
    #                low bound        n=3
    #        t:      nominal value    t=1.4398
    #                low bound        t>0.0
    #        tails:  value 1          tails = 1
    #                value 2          tails = 2
    #                missing tails
    #        output:
    #                The output is an interaction of t x tails x n:
    #                    nominal t, 1 tail
    #                    nominal t, 2 tails
    #                    low n, low t, 1 tail
    #                    low n, low t, 2 tails
    #                    high n, low t, 1 tail
    #                    high n, low t, 2 tails
    #                    low n, high t, 1 tail
    #                    low n, high t, 2 tails
    #                    high n, high t, 1 tail
    #                    high n, high t, 2 tails
    #                    nominal t, default tails
    #    Sad path analysis:
    #        n:      missing n
    #                out-of-bound n   n<3
    #                non-integer n    n = 2.5
    #        t:      missing t
    #                out-of-bounds n  t<0.0
    #                non-numeric t    t="abc"
    #        tails:  invalid tails    tails = 3
    #
    # Happy path
    def test100_010ShouldCalculateNominalCase1TailHttp(self):
        self.setT(1.8946)
        self.setN(7)
        self.setTails(1)
        self.setExtra("a")
        result = prob(self.inputDictionary)
        self.assertAlmostEqual(result[self.solutionKey], 0.950, 3)
      
    def test100_010ShouldCalculateNominalCase1Tail(self):
        self.setT(1.8946)
        self.setN(7)
        self.setTails(1)
        result = prob(self.inputDictionary)
        self.assertAlmostEqual(result[self.solutionKey], 0.950, 3)
   
    def test100_020ShouldCalculateNominalCase2Tail(self):
        self.setT(1.8946)
        self.setN(7)
        self.setTails(2)
        result = prob(self.inputDictionary)
        self.assertAlmostEqual(result[self.solutionKey], 0.900, 3)
   
    def test100_030ShouldCalculateLowNLowT1TailEdgeCase(self):
        self.setT(0.2767)
        self.setN(3)
        self.setTails(1)
        result = prob(self.inputDictionary)
        self.assertAlmostEqual(result[self.solutionKey], 0.600, 3)
   
    def test100_040ShouldCalculateLowNLowT2TailEdgeCase(self):
        self.setT(0.2767)
        self.setN(3)
        self.setTails(2)
        result = prob(self.inputDictionary)
        self.assertAlmostEqual(result[self.solutionKey], 0.200, 3)
   
    def test100_050ShouldCalculateHighNLowT1TailEdgeCase(self):
        self.setT(0.2567)
        self.setN(20)
        self.setTails(1)
        result = prob(self.inputDictionary)
        self.assertAlmostEqual(result[self.solutionKey], 0.600, 3)
   
    def test100_060ShouldCalculateHighNLowT2TailEdgeCase(self):
        self.setT(0.2567)
        self.setN(20)
        self.setTails(2)
        result = prob(self.inputDictionary)
        self.assertAlmostEqual(result[self.solutionKey], 0.200, 3)
   
    def test100_070ShouldCalculateLowNHighT1EdgeCase(self):
        self.setT(5.8409)
        self.setN(3)
        self.setTails(1)
        result = prob(self.inputDictionary)
        self.assertAlmostEqual(result[self.solutionKey], 0.995, 3)
   
    def test100_080ShouldCalculateLowNHighT2EdgeCase(self):
        self.setT(5.8409)
        self.setN(3)
        self.setTails(2)
        result = prob(self.inputDictionary)
        self.assertAlmostEqual(result[self.solutionKey], 0.990, 3)
   
    def test100_090ShouldCalculateHighHighT1TailEdgeCase(self):
        self.setT(2.8453)
        self.setN(20)
        self.setTails(1)
        result = prob(self.inputDictionary)
        self.assertAlmostEqual(result[self.solutionKey], 0.995, 3)
   
    def test100_100ShouldCalculateHighHighT2TailEdgeCase(self):
        self.setT(2.8453)
        self.setN(20)
        self.setTails(2)
        result = prob(self.inputDictionary)
        self.assertAlmostEqual(result[self.solutionKey], 0.990, 3)
   
    def test100_110ShouldCalculateWithDefaultTails(self):
        self.setT(1.8946)
        self.setN(7)
        result = prob(self.inputDictionary)
        self.assertAlmostEqual(result[self.solutionKey], 0.900, 3)
   
    # Sad path
    def test100_910ShouldRaiseExceptionOnMissingT(self):
        self.setN(self.nominalN)
        self.setTails(self.nominalTails)
        result = prob(self.inputDictionary)
        self.assertIn(self.errorKey, result)
        self.assertIn(self.errorValue, result[self.errorKey])
   
    def test100_920ShouldRaiseExceptionOnOutOfBoundsT(self):
        self.setT(-1.0)
        self.setN(self.nominalN)
        self.setTails(self.nominalTails)
        result = prob(self.inputDictionary)
        self.assertIn(self.errorKey, result)
        self.assertIn(self.errorValue, result[self.errorKey])
   
    def test100_930ShouldRaiseExceptionOnNonNumericT(self):
        self.setT("abc")
        self.setN(self.nominalN)
        self.setTails(self.nominalTails)
        result = prob(self.inputDictionary)
        self.assertIn(self.errorKey, result)
        self.assertIn(self.errorValue, result[self.errorKey])
   
    def test100_940ShouldRaiseExceptionOnInvalidTails(self):
        self.setTails(0)
        self.setT(self.nominalT)
        self.setN(self.nominalN)
        result = prob(self.inputDictionary)
        self.assertIn(self.errorKey, result)
        self.assertIn(self.errorValue, result[self.errorKey])
   
    def test100_950ShouldRaiseExceptionOnMissingN(self):
        self.setT(self.nominalT)
        self.setTails(1)
        result = prob(self.inputDictionary)
        self.assertIn(self.errorKey, result)
        self.assertIn(self.errorValue, result[self.errorKey])
   
    def test100_960ShouldRaiseExceptionOnOutOfBoundN(self):
        self.setN(0)
        self.setT(self.nominalT)
        self.setTails(1)
        result = prob(self.inputDictionary)
        self.assertIn(self.errorKey, result)
        self.assertIn(self.errorValue, result[self.errorKey])
   
    def test100_970ShouldRaiseExceptionOnNonIntegerN(self):
        self.setN(2.5)
        self.setT(self.nominalT)
        self.setTails(1)
        result = prob(self.inputDictionary)
        self.assertIn(self.errorKey, result)
        self.assertIn(self.errorValue, result[self.errorKey])
        
# ------------------------
    # inward facing test (unit tests)
    #     200 _integrate
    #     inputs:
    #          n: integer, .GE.3, mandatory, validated
    #          t: float > 0.0, mandatory, validated
    #         _f: function
    #     output:
    #         float .GE. 0.0
    # 
    # happy path analysis
    #     test 010: nominal n, nominal t 
    #     test 020: low bound n, nominal t 
    def test200_010NominalNnominalT(self):
        t = self.nominalT
        n = self.nominalN
        expectedResult = 1.03554
        result = _integrate(t, n, _f)
        self.assertAlmostEqual(expectedResult, result, 3)
    def test200_020lowNnominalT(self):
        t = self.nominalT
        n = 3
        expectedResult = 1.02632
        result = _integrate(t, n, _f)
        self.assertAlmostEqual(expectedResult, result, 3)
