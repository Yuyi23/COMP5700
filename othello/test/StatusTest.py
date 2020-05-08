from unittest import TestCase
from othello.status import _status as status
import json
import asyncio

class StatusTest(TestCase):
    def testAllNorminal010(self):
        parm = {'light':'1','dark':'2','blank':'0',
                'board': '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]',
                'integrity': '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'}
        result = status(parm)
        self.assertEqual(result,{'status': 'ok'})

    def testHighBoundLight020(self):
        parm = {'light':'9','dark':'2','blank':'0',
                'board':'[0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,0,0,0,0,2,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0]',
                'integrity':'5ab81cb67067273363db989119448a0b878896f7db5c268a50c4ae3062cb3647'}
        result = status(parm)
        self.assertEqual(result,{'status': 'ok'})
    
    def testLowBoundLight021(self):
        parm = {'light':'0','dark':'2','blank':'1',
                'board':'[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,2,1,1,1,1,2,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]',
                'integrity':'1b7e612b959852acbaf6b55d3f6b8dab2cdc32248a58a89dcf022ae80e5b36de'}
        result = status(parm)
        self.assertEqual(result,{'status': 'ok'})
    
    def testMissingLight022(self):
        parm = {'dark':'2','blank':'3',
                'board':'[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]',
                'integrity':'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a'}
        result = status(parm)
        self.assertEqual(result,{'status': 'ok'})
    
    def testLowBoundDark030(self):
        parm = {'light':'5','dark':'0','blank':'9',
                'board':'[9,9,9,9,9,9,9,9,9,9,9,9,9,9,5,0,9,9,9,9,0,5,9,9,9,9,9,9,9,9,9,9,9,9,9,9]',
                'integrity':'85c972c79b667135f99ad9380f4af4a7495c5b5de3768c9cb36c4bc73f0da08a'}
        result = status(parm)
        self.assertEqual(result,{'status': 'ok'})
    
    def testHighBoundDark031(self):
        parm = {'light':'5','dark':'9','blank':'3',
                'board':'[3,3,3,3,3,3,3,3,3,3,3,3,3,3,5,9,3,3,3,3,9,5,3,3,3,3,3,3,3,3,3,3,3,3,3,3]',
                'integrity':'34932b7f4bbafed18cf99e367e29407e6aae8b49b2ced711f31e429e7efc2a12'}
        result = status(parm)
        self.assertEqual(result,{'status': 'ok'})
    
    def testMissingDark032(self):
        parm = {'light':'5','blank':'3',
                'board':'[3,3,3,3,3,3,3,3,3,3,3,3,3,3,5,2,3,3,3,3,2,5,3,3,3,3,3,3,3,3,3,3,3,3,3,3]',
                'integrity':'a348c2dae89e65378fc64d889b1d394819c021b2e4cccb37310bbef9335bb900'}
        result = status(parm)
        self.assertEqual(result,{'status': 'ok'})
    
    def testLowBlank040(self):
        parm = {'light':'5','dark':'6','blank':'0',
                'board':'[0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,6,0,0,0,0,6,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0]',
                'integrity':'062f219e852404144cd7967bcbac5d5d82c151697d8eacfd8c29779acbc58b19'}
        result = status(parm)
        self.assertEqual(result,{'status': 'ok'})
    
    def testHighBlank041(self):
        parm = {'light':'5','dark':'6','blank':'9',
                'board':'[9,9,9,9,9,9,9,9,9,9,9,9,9,9,5,6,9,9,9,9,6,5,9,9,9,9,9,9,9,9,9,9,9,9,9,9]',
                'integrity':'5b698f38d9d1c1754df196ee688f3900ceba9d074cb74b5e17c19a197b69bf02'}
        result = status(parm)
        self.assertEqual(result,{'status': 'ok'})
        
    def testMissingBlank042(self):
        parm = {'light':'5','dark':'6',
                'board':'[0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,6,0,0,0,0,6,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0]',
                'integrity':'062f219e852404144cd7967bcbac5d5d82c151697d8eacfd8c29779acbc58b19'}
        result = status(parm)
        self.assertEqual(result,{'status': 'ok'})
    
    def testLowSize050(self):
        parm = {'light':'1','dark':'2','blank':'0',
                'board':'[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]',
                'integrity':'6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'}
        result = status(parm)
        self.assertEqual(result,{'status': 'ok'})
        
    def testHighSize051(self):
        parm = {'light':'1','dark':'2','blank':'0',
                'board':'[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]',
                'integrity':'5df1fd1ccbd0dc74d65ab00d4d62f2e21c2def95dc47e7c73751986cdb5e8710'}
        result = status(parm)
        self.assertEqual(result,{'status': 'ok'})
        
    def testDarkNext060(self):
        parm = {'light':'1','dark':'2','blank':'3',
                'board':'[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]',
                'integrity':'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a'}
        result = status(parm)
        self.assertEqual(result,{'status': 'ok'})
        
    def testLightNext061(self):
        parm = {'light':'1','dark':'2','blank':'3',
                'board':'[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3]',
                'integrity':'66271cbb9037c515e73be3a74a37259a179f2d2861cf4e82130cd579a2141093'}
        result = status(parm)
        self.assertEqual(result,{'status': 'ok'})
        
    def testOK070(self):
        parm = {'light':'1','dark':'2','blank':'0',
                'board':'[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]',
                'integrity':'6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'}
        result = status(parm)
        self.assertEqual(result,{'status': 'ok'})
        
    def testDarkOnly071(self):
        parm = {'light':'1','dark':'2','blank':'0',
                'board':'[0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,0,1,1,1,1,0]',
                'integrity':'e2f7b8593ebadc126833074a7d8653d3c12c36ab3b7622a9cc6ac5dc1a0d9698'}
        result = status(parm)
        self.assertEqual(result,{'status': 'dark'})
    
    def testLightOnly072(self):
        parm = {'light':'1','dark':'2','blank':'3',
                'board':'[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]',
                'integrity':'7c53df9ff782bbbff544d876f4d69a1d87d5864295c0e4a6bf29e6a7ee5a96fc'}
        result = status(parm)
        self.assertEqual(result,{'status': 'light'})
        
    def testEnd072(self):
        parm = {'light':'1','dark':'2','blank':'0',
                'board':'[1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0, 1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,2,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1]',
                'integrity':'8a1c0659575e8cdd01b2e4ff3f431c845e7e7960279bb7abfaa5465e4a755354'}
        result = status(parm)
        self.assertEqual(result,{'status': 'end'})                      
    
    def testAboveBoundLight900(self):
        parm = {'light':'10','dark':'2','blank':'1',
                'board':'[1,1,1,1,1,1,1,1,1,1,1,1,1,1,10,2,1,1,1,1,2,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1]',
                'integrity':'b71bf3bee30fb8c3caa49752bcf9656870cfbd3bec4e4353e1e491054bf11c2f'}
        result = status(parm)
        self.assertEqual(result,{'status': 'error: light is above bound'}) 
    
    def testBelowBoundLight901(self):
        parm = {'light':'-1','dark':'2','blank':'1',
                'board':'[1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,2,1,1,1,1,2,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]',
                'integrity':'f31631fdc7ba5ecd3096a306dbc7e43a9bc13fa781b91d83c36057f5050a51da'}
        result = status(parm)
        self.assertEqual(result,{'status': 'error: light is below bound'}) 
        
    def testNonIntegerLight902(self):
        parm = {'light':'X','dark':'2','blank':'1',
                'board':'[1,1,1,1,1,1,1,1,1,1,1,1,1,1,X,2,1,1,1,1,2,X,1,1,1,1,1,1,1,1,1,1,1,1,1,1]',
                'integrity':'8959fc376b23af1520014ef3bef1eb4f924ec692bbbcd9f638245bf85fb0a6da'}
        result = status(parm)
        self.assertEqual(result,{'status': 'error: light is not integer'}) 
    
    def testNullLight903(self):
        parm = {'light':'','dark':'2','blank':'1',
                'board':'[1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,1,1,1,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1]',
                'integrity':'1cc0050055aa122edbb536cc63dfe515e6a55132a42a6c8fa41349ab6e572c6a'}
        result = status(parm)
        self.assertEqual(result,{'status': 'error: light is null'}) 
    
    def testAboveBoundDark910(self):
        parm = {'light':'5','dark':'10','blank':'1',
                'board':'[1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,10,1,1,1,1,10,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1]',
                'integrity':'e8a244c301df58429d82070942fe05dff389162c0aeec8383e3c82863ae09c62'}
        result = status(parm)
        self.assertEqual(result,{'status': 'error: dark is above bound'})     
    
    def testBelowBoundDark911(self):
        parm = {'light':'5','dark':'-1','blank':'1',
                'board':'[1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,-1,1,1,1,1,-1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1]',
                'integrity':'301e0f00c1b83b65adc1d4fd5e87aaf7f594aa20842ab1df86a6be2e144367db'}
        result = status(parm)
        self.assertEqual(result,{'status': 'error: dark is below bound'})  
    
    def testNonIntegerLight912(self):
        parm = {'light':'5','dark':'1.2','blank':'1',
                'board':'[1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1.2,1,1,1,1,1.2,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1]',
                'integrity':'e62a2ec6eb082391a6a5664b4f4dbd8130e43d6589267b19b831423bfcde4a9d'}
        result = status(parm)
        self.assertEqual(result,{'status': 'error: dark is not integer'})  
    
    def testNullDark913(self):
        parm = {'light':'1','dark':'','blank':'3',
                'board':'[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]',
                'integrity':'5d5aeb4a45b57eecf69dcc304664fcf7a6f7c74c86ef9ede14da46ab2d9df242'}
        result = status(parm)
        self.assertEqual(result,{'status': 'error: dark is null'})  
        
    def testAboveBoundBlank920(self):
        parm = {'light':'1','dark':'2','blank':'10',
                'board':'[10,10,10,10,10,10,10,10,10,10,10,10,10,10,1,2,10,10,10,10,2,1,10,10,10,10,10,10,10,10,10,10,10,10,10,10]',
                'integrity':'530242aec98aa07d3c025b9101bd5b840527cd9b03302641da18c801d70c37e8'}
        result = status(parm)
        self.assertEqual(result,{'status': 'error: blank is above bound'}) 
    
    def testBelowBoundBlank921(self):
        parm = {'light':'1','dark':'2','blank':'-1',
                'board':'[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,2,-1,-1,-1,-1,2,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]',
                'integrity':'2e226315d3fc18cf5771b45ae78bfe7be9510ee98b6e566e382f8a70861c8e7d'}
        result = status(parm)
        self.assertEqual(result,{'status': 'error: blank is below bound'})
        
    def testNonIntegerBlank922(self):
        parm = {'light':'1','dark':'2','blank':'1E5',
                'board':'[1E5,1E5,1E5,1E5,1E5,1E5,1E5,1E5,1E5,1E5,1E5,1E5,1E5,1E5,1,2,1E5,1E5,1E5,1E5,2,1,1E5,1E5,1E5,1E5,1E5,1E5,1E5,1E5,1E5,1E5,1E5,1E5,1E5,1E5]',
                'integrity':'fe62b7f99befb02e21c50cc755a68ef80fb59d56224b02a1f2888e0830454773'} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: blank is not integer'})
    
    def testNullBlank923(self):
        parm = {'light':'1','dark':'2','blank':'',
                'board':'[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]',
                'integrity':'6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: blank is null'})
        
    def testNonSquareBoard930(self):
        parm = {'light':'1','dark':'2','blank':'3',
                'board':'[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3]',
                'integrity':'9d43a04297202bccc81a13b6857179269c0fe33e5227c6569286d54d82493ba6'} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: board is non square'})
        
    def testOddBoard933(self):
        parm = {'light':'1','dark':'2','blank':'3',
                'board':'[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]',
                'integrity':'1e3f8bb2d56c5b4483c9f3dccf7bc16d339534a98020e9a28383aaa219f3e64d'} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: board is odd'})
        
    def testMissingBoard934(self):
        parm = {'light':'1','dark':'2','blank':'3',
                'integrity':'1e3f8bb2d56c5b4483c9f3dccf7bc16d339534a98020e9a28383aaa219f3e64d'} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: board is missing'})
    
    def testNullBoard935(self):
        parm = {'light':'1','dark':'2','blank':'3',
                'board':'',
                'integrity':'1e3f8bb2d56c5b4483c9f3dccf7bc16d339534a98020e9a28383aaa219f3e64d'} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: board is null'})
    
    def testShortIntegrity940(self):
        parm = {'light':'1','dark':'2','blank':'3',
                'board':'[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]',
                'integrity':'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465'} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: integrity'})
        
    def testLongIntegrity941(self):
        parm = {'light':'1','dark':'2','blank':'3',
                'board':'[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]',
                'integrity':'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a00'} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: integrity'})
        
    def testNonHexIntegrity942(self):
        parm = {'light':'1','dark':'2','blank':'3',
                'board':'[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]',
                'integrity':'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465$'} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: integrity'})
    
    def testMissingIntegrity943(self):
        parm = {'light':'1','dark':'2','blank':'3',
                'board':'[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]'} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: integrity'})
    
    def testNullIntegrity944(self):
        parm = {'light':'1','dark':'2','blank':'3',
                'board':'[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]',
                'integrity':''} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: integrity'})
    
    def testLightEqualDark950(self):
        parm = {'light':'2','dark':'2','blank':'0',
                'board':'[0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]',
                'integrity':'e50f93033edd2b27fd1c54631a4b574e545df9e8c06e0b4f74ca94841a4ab6c4'} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: light is equal to dark'})
    
    def testBlankEquallight951(self):
        parm = {'light':'1','dark':'2','blank':'1',
                'board':'[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]',
                'integrity':'c725061d80e342070c231d2b987c476f92b8f3d9e5826c2223cff281562e8e2c'} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: light is equal to blank'})
        
    def testBlankEqualDark952(self):
        parm = {'light':'1','dark':'2','blank':'2',
                'board':'[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2]',
                'integrity':'4edfe0aad5d491d98b8103e4f8f899cd3cef690f6ec3602a16e5a0e0301e8bd6'} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: dark is equal to blank'})
    
    def testInvalidIntegrity954(self):
        parm = {'light':'1','dark':'2','blank':'3',
                'board':'[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]',
                'integrity':'4d5aeb4a45b57eecf69dcc304664fcf7a6f7c74c86ef9ede14da46ab2d9df242'} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: integrity'})
    
    def testBoardwithNontokens955(self):
        parm = {'light':'1','dark':'2','blank':'3',
                'board':'[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]',
                'integrity':'c9fd7c0049f79f33e45998064cd1fca01600dd5cdc55cb3bf33169cd07c1905a'} 
        result = status(parm)
        self.assertEqual(result,{'status': 'error: board'})

    
