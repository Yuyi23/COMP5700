from unittest import TestCase
from othello.create import _create as create
import json
import asyncio

class CreateTest(TestCase):
    #happy test
    def testAllNorminal010(self):
        parm = {'size':'10','light':'6','dark':'5','blank':'1'}
        result = create(parm)
        self.assertEqual(result, {'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 5, 1, 1, 1, 1, 1, 1, 1, 1, 5, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                                   'tokens': {'light': 6, 'dark': 5, 'blank': 1}, 
                                   'status': 'ok', 
                                   'integrity': 'd0f18c5b412ab1dbf89da19baa33cc35f4a7dd0619ce7b7dcb2381d2cb14a412'})
    
    def testHighLight020(self):
        parm = {'size':'10','light':'9','dark':'5','blank':'1'}
        result = create(parm)
        self.assertEqual(result, {'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 5, 1, 1, 1, 1, 1, 1, 1, 1, 5, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                                  'tokens': {'light': 9, 'dark': 5, 'blank': 1}, 
                                  'status': 'ok', 
                                  'integrity': '723c769319c6529cf8520336232a9e5d281be77df1455c6ceb10a5d1d4733236'})
    
    def testLowLight021(self):
        parm = {'size':'10','light':'0','dark':'5','blank':'1'}
        result = create(parm)
        self.assertEqual(result,{'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 5, 1, 1, 1, 1, 1, 1, 1, 1, 5, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                                 'tokens': {'light': 0, 'dark': 5, 'blank': 1}, 
                                 'status': 'ok', 
                                 'integrity': '4bd2efa7e0d5f13551f7277950e45b6fcfe7d5159b80823a5dcbdf57abb4d83a'})
    
    def testMissingLight022(self):
        parm = {'size':'10','dark':'5','blank':'3'}
        result = create(parm)
        self.assertEqual(result,{'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 5, 3, 3, 3, 3, 3, 3, 3, 3, 5, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 
                                 'tokens': {'light': 1, 'dark': 5, 'blank': 3}, 
                                 'status': 'ok', 
                                 'integrity': 'f211a92f576794a821bb24f359739b8b42a6a16634005a1e4b32313a6575e2be'})
   
    def testHighDark030(self):
        parm = {'size':'10','light':'3','dark':'9','blank':'4'}
        result = create(parm)
        self.assertEqual(result,{'board': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 9, 4, 4, 4, 4, 4, 4, 4, 4, 9, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 
                                 'tokens': {'light': 3, 'dark': 9, 'blank': 4}, 
                                 'status': 'ok', 
                                 'integrity': 'a3718ffbc2f822320ee4db10c269a9749859b9952db13ff6b289a6ebd6ce42c6'})
    
    def testLowDark031(self):
        parm = {'size':'10','light':'3','dark':'0','blank':'4'}
        result = create(parm)
        self.assertEqual(result,{'board': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 
                                 'tokens': {'light': 3, 'dark': 0, 'blank': 4}, 
                                 'status': 'ok', 
                                 'integrity': '7bf98e8385a158097f52361dac139bb5882f3eaa48e8146d72d65de5981d2e5e'})
    
    def testMissingDark032(self):
        parm = {'size':'10','light':'3','blank':'4'}
        result = create(parm)
        self.assertEqual(result,{'board': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 
                                 'tokens': {'light': 3, 'dark': 2, 'blank': 4}, 
                                 'status': 'ok', 
                                 'integrity': '71f91a7d487c9e9ad69a43269c6a90c449f97fd93848b8493e47a2f6054e7c82'})
    
    def testHighBlank040(self):
        parm = {'size':'10','light':'3','dark':'4','blank':'9'}
        result = create(parm)
        self.assertEqual(result,{'board': [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3, 4, 9, 9, 9, 9, 9, 9, 9, 9, 4, 3, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 
                                 'tokens': {'light': 3, 'dark': 4, 'blank': 9}, 
                                 'status': 'ok', 
                                 'integrity': '5b4c82af0cf6a72ab1938b8e5a3c1ce413b9db583d0f974703954427413021d0'})
    
    def testLowBlank041(self):
        parm = {'size':'10','light':'3','dark':'4','blank':'0'}
        result = create(parm)
        self.assertEqual(result, {'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                  'tokens': {'light': 3, 'dark': 4, 'blank': 0}, 
                                  'status': 'ok', 
                                  'integrity': 'eeaa1d4229234a1453901319e7f584a337595d6d332a22a76c4aae8888cde9d6'})
    
    def testMissingBlank042(self):
        parm = {'size':'10','light':'3','dark':'4'}
        result = create(parm)
        self.assertEqual(result,{'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 'tokens': {'light': 3, 'dark': 4, 'blank': 0}, 
                                 'status': 'ok', 
                                 'integrity': 'eeaa1d4229234a1453901319e7f584a337595d6d332a22a76c4aae8888cde9d6'})
    
    def testHighBound050(self):
        parm = {'size':'16','light':'3','dark':'4','blank':'5'}
        result = create(parm)
        self.assertEqual(result,{'board': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 
                                 'tokens': {'light': 3, 'dark': 4, 'blank': 5}, 
                                 'status': 'ok', 
                                 'integrity': '682b1bac788017f23b846862ce44f2c3efe03a22f49de36085e0e57fc6957416'})
   
    def testLowBound051(self):
        parm = {'size':'6','light':'3','dark':'4','blank':'5'}
        result = create(parm)
        self.assertEqual(result,{'board': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 4, 5, 5, 5, 5, 4, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 
                                 'tokens': {'light': 3, 'dark': 4, 'blank': 5}, 
                                 'status': 'ok', 
                                 'integrity': 'b87b212e557d1dc1080f1c6e380bab404ae8cffa048b86e649e54c620f0d9c6a'})
    
    def testMissingBound052(self):
        parm = {'light':'3','dark':'4','blank':'5'}
        result = create(parm)
        self.assertEqual(result,{'board': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 4, 5, 5, 5, 5, 5, 5, 4, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                                 'tokens': {'light': 3, 'dark': 4, 'blank': 5}, 
                                 'status': 'ok', 
                                 'integrity': '306a2474c8f8b41c9e31af0fe360f9fcaf3531b3b4a1c3624acd8fbc2530b02e'})
    
    def testDefault060(self):
        parm = {}
        result = create(parm)
        self.assertEqual(result,{'board': [0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,1,2,0,0,0, 0,0,0,2,1,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0],
                                 'tokens': {'light': 1,'dark': 2, 'blank': 0},
                                 'integrity': 'b11fcf5f9ac9d3b8cea8085208e210182a8d6b73a84028562ab2c87d190b9ada',
                                 'status':'ok'})
    
    def testExtraneous070(self):
        parm = {'extra':'1234'}
        result = create(parm)
        self.assertEqual(result,{'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 'tokens': {'light': 1, 'dark': 2, 'blank': 0}, 
                                 'status': 'ok', 
                                 'integrity': 'b11fcf5f9ac9d3b8cea8085208e210182a8d6b73a84028562ab2c87d190b9ada'})
    
    #sad test
    def testAboveBoundLight900(self):
        parm = {'light':'10'} 
        result = create(parm)
        self.assertEqual(result,{'status': 'error: light is above bound'})
    
    def testBelowBoundLight901(self):
        parm = {'light':'-1'} 
        result = create(parm)
        self.assertEqual(result,{'status': 'error: light is below bound'})
    
    def testNonIntegerLight902(self):
        parm = {'light':'w'} 
        result = create(parm)
        self.assertEqual(result,{'status': 'error: light is not integer'})
    
    def testNullLight903(self):
        parm = {'light': ''} 
        result = create(parm)
        self.assertEqual(result,{'status': 'error: light is null'})
    
    def testAboveBoundDark910(self):
        parm = {'dark':'10'} 
        result = create(parm)
        self.assertEqual(result,{'status': 'error: dark is above bound'})
    
    def testBelowBoundDark911(self):
        parm = {'dark':'-1'} 
        result = create(parm)
        self.assertEqual(result,{'status': 'error: dark is below bound'})
    
    def testNonIntegerLight912(self):
        parm = {'dark':'d'} 
        result = create(parm)
        self.assertEqual(result,{'status': 'error: dark is not integer'})
   
    def testNullDark913(self):
        parm = {'dark': ''} 
        result = create(parm)
        self.assertEqual(result,{'status': 'error: dark is null'})
    
    def testAboveBoundBlank920(self):
        parm = {'blank':'10'} 
        result = create(parm)
        self.assertEqual(result,{'status': 'error: blank is above bound'})
    
    def testBelowBoundBlank921(self):
        parm = {'blank':'-1'} 
        result = create(parm)
        self.assertEqual(result,{'status': 'error: blank is below bound'})
    
    def testNonIntegerBlank922(self):
        parm = {'blank':'b'} 
        result = create(parm)
        self.assertEqual(result,{'status': 'error: blank is not integer'})
    
    def testNullBlank923(self):
        parm = {'blank': ''} 
        result = create(parm)
        self.assertEqual(result,{'status': 'error: blank is null'})
    
    def testAboveBoundSize930(self):
        parm = {'size':'17'} 
        result = create(parm)
        self.assertEqual(result,{'status': 'error: size is above bound'})
    
    def testBelowBoundSize931(self):
        parm = {'size':'5'} 
        result = create(parm)
        self.assertEqual(result,{'status': 'error: size is below bound'})
    
    def testOddSize933(self):
        parm = {'size':'9'}
        result = create(parm)
        self.assertEqual(result,{'status': 'error: size is odd'})
    
    def testNonIntegerSize932(self):
        parm = {'size':'1.2'}
        result = create(parm)
        self.assertEqual(result,{'status': 'error: size is not integer'})
    
    def testNullSize934(self):
        parm = {'size': ''} 
        result = create(parm)
        self.assertEqual(result,{'status': 'error: size is null'})
    
    def testLightEqualDark940(self):
        parm = {'light': '5','dark':'5','blank':'0'}
        result = create(parm)
        self.assertEqual(result,{'status': 'error: light is equal to dark'})
    
    def testLightEqualBlank941(self):
        parm = {'light': '5','dark':'2','blank':'5'}
        result = create(parm)
        self.assertEqual(result,{'status': 'error: light is equal to blank'})
    
    def testDarkEqualBlank942(self):
        parm = {'light': '1','dark':'2','blank':'2'}
        result = create(parm)
        self.assertEqual(result,{'status': 'error: dark is equal to blank'})