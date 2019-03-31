# CSE 101 - IP HW2
# K-Map Minimization 
# Name:Rohith Rajesh
# Roll Number:2018182
# Section:A
# Group:6
# Date:7/10/2018




import unittest
from HW2_2018182 import minFunc



class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual(minFunc(3,'(3,4,5,6) d-'),"x'yz + xy' + xz'")
		self.assertEqual(minFunc(4,'(3,4,5,6,10,11) d(8,9,14)'),"w'xy' + wyz' + x'yz + xyz'")
		self.assertEqual(minFunc(4,'(3,4,5,6,10,11,1,2,7,8,9,12,13,14,15,0) d-'),"1")
		self.assertEqual(minFunc(2,'(0,1) d(2)'),"y'")
		self.assertEqual(minFunc(3,'(3,4,5,6) d(2)'),"x'y + xy' + xz'")

                
if __name__=='__main__':
	unittest.main()
