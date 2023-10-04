import unittest

def check(name):

    return name == "MIGUEL"

class myTest(unittest.TestCase):

    def test(self):
            
        self.assertTrue(check('MIGUEL'))

if __name__=='__main__':
    
    unittest.main() 
