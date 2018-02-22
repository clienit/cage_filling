# -*- coding: utf-8 -*-
import unittest
from cage import Cage 

class TestCage(unittest.TestCase):
    
    def setUp(self):
        """ Initialize first cage for test 1 """
        self.cage_1 = Cage()
        self.cage_1.height = 0
        self.cage_1.width = 0       
        self.cage_1.length = 0
        self.cage_1.volume = 0
        self.cage_1.packages =[]
        
        """ Create packages for test 1 """
        self.package_1 = [10, 10, 830, 83000]
        self.package_2 = [10, 10, 10, 1000]
        self.package_3 = [10, 10, 7, 700]
        
        """ Initialize second cage for test 2 """
        self.cage_2 = Cage()
        self.cage_2.height = 0
        self.cage_2.width = 0       
        self.cage_2.length = 0
        self.cage_2.volume = 0
        self.cage_2.packages =[]
        
        """ Create packages for test 2 """
        self.package_4 = [10, 10, 10, 1000]
        self.package_5 = [10, 10, 10, 1000]

        """ Initialize second cage for test 3 """
        self.cage_3 = Cage()
        self.package_6 = [300, 500, 400, 60000000]
        self.package_7 = [300, 500, 400, 60000000] 
        self.package_8 = [153, 268, 398, 16319592] 
        self.package_9 = [112, 325, 157, 5714800] 
        self.package_10 = [112, 325, 157, 5714800] 
        self.package_11 = [100, 100, 100, 1000000]
        self.package_12 = [60, 167, 100, 1002000] 
        
    def tearDown(self):
        pass
    
    def test_append(self):
        """ Test appending 3 boxes if they are put into correct place """
        self.cage_1.append(self.package_1)
        self.assertEqual(self.cage_1.height,10)
        self.assertEqual(self.cage_1.width,10)
        self.assertEqual(self.cage_1.length,830)
        self.assertEqual(self.cage_1.volume,83000)
        
        self.cage_1.append(self.package_2)
        self.assertEqual(self.cage_1.height,10)
        self.assertEqual(self.cage_1.width,10)
        self.assertEqual(self.cage_1.length,840)
        self.assertEqual(self.cage_1.volume,84000)
        
        self.cage_1.append(self.package_3)
        self.assertEqual(self.cage_1.height,10)
        self.assertEqual(self.cage_1.width,20)
        self.assertEqual(self.cage_1.length,840)
        self.assertEqual(self.cage_1.volume,84700)
        
        """ Test appending 2 boxes if they are put into correct place """
        self.cage_2.append(self.package_4)
        self.assertEqual(self.cage_2.height,10)
        self.assertEqual(self.cage_2.width,10)
        self.assertEqual(self.cage_2.length,10)
        self.assertEqual(self.cage_2.volume,1000)
        
        self.cage_2.append(self.package_4)
        self.assertEqual(self.cage_2.height,10)
        self.assertEqual(self.cage_2.width,10)
        self.assertEqual(self.cage_2.length,20)
        self.assertEqual(self.cage_2.volume,2000)
        
        """ Test appending 7 boxes if they are put into correct place """
        self.cage_3.append(self.package_6)
        self.assertEqual(self.cage_3.height,300)
        self.assertEqual(self.cage_3.width,500)
        self.assertEqual(self.cage_3.length,400)
        self.assertEqual(self.cage_3.volume,60000000)
        
        self.cage_3.append(self.package_7)
        self.assertEqual(self.cage_3.height,300)
        self.assertEqual(self.cage_3.width,500)
        self.assertEqual(self.cage_3.length,800)
        self.assertEqual(self.cage_3.volume,120000000)
        
        # [153, 268, 398, 16319592]       
        self.cage_3.append(self.package_8)
        self.assertEqual(self.cage_3.height,453)
        self.assertEqual(self.cage_3.width,268)
        self.assertEqual(self.cage_3.length,398)
        self.assertEqual(self.cage_3.volume,136319592)
        
        # [112, 325, 157, 5714800]  h - w - l    
        self.cage_3.append(self.package_9)
        self.assertEqual(self.cage_3.height,453)
        self.assertEqual(self.cage_3.width,593)
        self.assertEqual(self.cage_3.length,398)
        self.assertEqual(self.cage_3.volume,142034392)
        
        # [112, 325, 157, 5714800]  h - w - l    
        self.cage_3.append(self.package_10)
        self.assertEqual(self.cage_3.height,453)
        self.assertEqual(self.cage_3.width,593)
        self.assertEqual(self.cage_3.length,555)
        self.assertEqual(self.cage_3.volume,147749192)
        
        # [100, 100, 100, 1000000]  h - w - l    
        self.cage_3.append(self.package_11)
        self.assertEqual(self.cage_3.height,453)
        self.assertEqual(self.cage_3.width,593)
        self.assertEqual(self.cage_3.length,655)
        self.assertEqual(self.cage_3.volume,148749192)   
        
        # [60, 167, 100, 1002000]  h - w - l    
        self.cage_3.append(self.package_12)
        self.assertEqual(self.cage_3.height,453)
        self.assertEqual(self.cage_3.width,593)
        self.assertEqual(self.cage_3.length,755)
        self.assertEqual(self.cage_3.volume,149751192)         

        
if __name__ == '__main__':
    unittest.main()