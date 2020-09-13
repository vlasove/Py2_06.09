import funcs 

if funcs.add(2,3) != 5 :
    raise Exception("ERROR! add(2,3)")
else:
    print("Test pass! add(2,3) == 5")


    
if funcs.sub(5,2) != 3 :
    raise Exception("ERROR! sub(5,2)")
else:
    print("Test pass! sub(5,2) == 3")


import unittest 

class TestFuncs(unittest.TestCase):
    def test_add(self):
        pass 

    def test_sub(self):
        pass 

if __name__ == "__main__":
    unittest.run()