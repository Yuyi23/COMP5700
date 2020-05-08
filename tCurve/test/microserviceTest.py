from unittest import TestCase
from tCurve.prob import prob
import http.client
from urllib.parse import urlencode
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
        self.PATH = '/prob?'
        self.PORT = 5000
        self.URL = 'localhost'

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
        
    def prob(self, parm):
        '''Issue HTTP Get and return result, which will be JSON string'''
        try:
            theParm = urlencode(parm)
            theConnection = http.client.HTTPConnection(self.URL, self.PORT)
            theConnection.request("GET", self.PATH + theParm)
            theStringResponse = str(theConnection.getresponse().read(),"utf-8")
        except Exception as e:
            theStringResponse = "{'diagnostic': '" + str(e) + "'}"
        return theStringResponse
        
    def string2dict(self, httpResponse):
        '''Convert JSON string to dictionary'''
        result = {}
        try:
            jsonString = httpResponse.replace("'", "\"")
            unicodeDictionary = json.loads(jsonString)
            for element in unicodeDictionary:
                if(isinstance(unicodeDictionary[element],str)):
                    result[str(element)] = str(unicodeDictionary[element])
                else:
                    result[str(element)] = unicodeDictionary[element]
        except Exception as e:
            result['diagnostic'] = str(e)
        return result


    # 100 prob
    #    Desired level of confidence:    boundary value analysis
    #    Input-output Analysis
    #        inputs:        n -> integer, .GE.3 &.LE. 30, mandatory, unvalidated
    #                       t -> float .GT. 0.0, mandatory, unvalidated
    #                       tails -> integer, 1 or 2, optional, defaults to 1
    #        outputs:    float .GT. 0 .LE. 1.0
    #    Happy path analysis (inter-domain):
    #        n:      nominal value    
    #                low bound        
    #                high bound       
    #        t:      nominal value    
    #                low bound        
    #                high bound       
    #        tails:  value 1          
    #                value 2          
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
    #
    #    Happy path analysis (extra-domain):
    #        extra parms ignored
    #
    #    Sad path analysis (inter-domain):
    #        n:      missing n
    #                out-of-low-bound n   
    #                out-of-high-bound n   
    #                non-integer n    
    #        t:      missing t
    #                out-of-bounds n  
    #                non-numeric t    
    #        tails:  invalid tails 
    #
    #    Sad path analysis (extra-domain):
    #        n:      present n parm, but missing value
    #        t:      present t parm, but missing value
    #        tails:  present tails parm, but missing value
    #
    # Happy path (inter-domain)
    def test100_010ShouldCalculateNominalCase1Tail(self):
        self.setT(1.8946)
        self.setN(7)
        self.setTails(1)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertAlmostEqual(resultDictionary[self.solutionKey], 0.950, 3)
  
    def test100_020ShouldCalculateNominalCase2Tail(self):
        self.setT(1.8946)
        self.setN(7)
        self.setTails(2)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertAlmostEqual(resultDictionary[self.solutionKey], 0.900, 3)
  
    def test100_030ShouldCalculateLowNLowT1TailEdgeCase(self):
        self.setT(0.2767)
        self.setN(3)
        self.setTails(1)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertAlmostEqual(resultDictionary[self.solutionKey], 0.600, 3)
  
    def test100_040ShouldCalculateLowNLowT2TailEdgeCase(self):
        self.setT(0.2767)
        self.setN(3)
        self.setTails(2)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertAlmostEqual(resultDictionary[self.solutionKey], 0.200, 3)
  
    def test100_050ShouldCalculateHighNLowT1TailEdgeCase(self):
        self.setT(0.2567)
        self.setN(20)
        self.setTails(1)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertAlmostEqual(resultDictionary[self.solutionKey], 0.600, 3)
  
    def test100_060ShouldCalculateHighNLowT2TailEdgeCase(self):
        self.setT(0.2567)
        self.setN(20)
        self.setTails(2)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertAlmostEqual(resultDictionary[self.solutionKey], 0.200, 3)
  
    def test100_070ShouldCalculateLowNHighT1EdgeCase(self):
        self.setT(5.8409)
        self.setN(3)
        self.setTails(1)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertAlmostEqual(resultDictionary[self.solutionKey], 0.995, 3)
  
    def test100_080ShouldCalculateLowNHighT2EdgeCase(self):
        self.setT(5.8409)
        self.setN(3)
        self.setTails(2)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertAlmostEqual(resultDictionary[self.solutionKey], 0.990, 3)
  
    def test100_090ShouldCalculateHighNHighT1TailEdgeCase(self):
        self.setT(2.8453)
        self.setN(20)
        self.setTails(1)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertAlmostEqual(resultDictionary[self.solutionKey], 0.995, 3)
  
    def test100_100ShouldCalculateHighNHighT2TailEdgeCase(self):
        self.setT(2.8453)
        self.setN(20)
        self.setTails(2)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertAlmostEqual(resultDictionary[self.solutionKey], 0.990, 3)
  
    def test100_110ShouldCalculateWithDefaultTails(self):
        self.setT(1.8946)
        self.setN(7)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertAlmostEqual(resultDictionary[self.solutionKey], 0.900, 3)
        
    # Happy path (extra-domain)
    def test100_120ShouldIgnoreExtraParms(self):
        self.setT(1.8946)
        self.setN(7)
        self.setTails(1)
        self.setExtra("a")
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertAlmostEqual(resultDictionary[self.solutionKey], 0.950, 3)
     
    # Sad path (inter-domain)
    def test100_910ShouldRaiseErrorOnMissingT(self):
        self.setN(self.nominalN)
        self.setTails(self.nominalTails)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertIn(self.errorKey, resultDictionary)
        self.assertIn(self.errorValue, resultDictionary[self.errorKey])
  
    def test100_920ShouldRaiseErrorOnOutOfBoundsT(self):
        self.setT(-1.0)
        self.setN(self.nominalN)
        self.setTails(self.nominalTails)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertIn(self.errorKey, resultDictionary)
        self.assertIn(self.errorValue, resultDictionary[self.errorKey])
  
    def test100_930ShouldRaiseErrorOnNonNumericT(self):
        self.setT("abc")
        self.setN(self.nominalN)
        self.setTails(self.nominalTails)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertIn(self.errorKey, resultDictionary)
        self.assertIn(self.errorValue, resultDictionary[self.errorKey])
  
    def test100_940ShouldRaiseErrorOnInvalidTails(self):
        self.setTails(0)
        self.setT(self.nominalT)
        self.setN(self.nominalN)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertIn(self.errorKey, resultDictionary)
        self.assertIn(self.errorValue, resultDictionary[self.errorKey])
  
    def test100_950ShouldRaiseErrorOnMissingN(self):
        self.setT(self.nominalT)
        self.setTails(self.nominalTails)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertIn(self.errorKey, resultDictionary)
        self.assertIn(self.errorValue, resultDictionary[self.errorKey])
  
    def test100_960ShouldRaiseErrorOnOutOfBoundN(self):
        self.setN(0)
        self.setT(self.nominalT)
        self.setTails(self.nominalTails)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertIn(self.errorKey, resultDictionary)
        self.assertIn(self.errorValue, resultDictionary[self.errorKey])
  
    def test100_970ShouldRaiseErrorOnNonIntegerN(self):
        self.setN(2.5)
        self.setT(self.nominalT)
        self.setTails(self.nominalTails)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertIn(self.errorKey, resultDictionary)
        self.assertIn(self.errorValue, resultDictionary[self.errorKey])
         
    # Sad path (extra-domain)
    def test100_980ShouldRaiseErrorOnNoValueN(self):
        self.setN('')
        self.setT(self.nominalT)
        self.setTails(self.nominalTails)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertIn(self.errorKey, resultDictionary)
        self.assertIn(self.errorValue, resultDictionary[self.errorKey])
          
    def test100_990ShouldRaiseErrorOnNoValueT(self):
        self.setN(self.nominalN)
        self.setT('')
        self.setTails(self.nominalTails)
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertIn(self.errorKey, resultDictionary)
        self.assertIn(self.errorValue, resultDictionary[self.errorKey])
         
    def test100_995ShouldRaiseErrorOnNoValueTails(self):
        self.setN(self.nominalN)
        self.setT(self.nominalT)
        self.setTails('')
        result = self.prob(self.inputDictionary)
        resultDictionary = self.string2dict(result)
        self.assertIn(self.errorKey, resultDictionary)
        self.assertIn(self.errorValue, resultDictionary[self.errorKey])
        