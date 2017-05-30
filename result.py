# open files for reading 

from mesh import obj 
from OpenGL.GL import *


first = obj.Obj("object_A.obj") 
second= obj.Obj("object_B.obj") 
class OBJ:
	"""docstring for OBJ"""
	def __init__(self, first,swapyz):
		
		self.Ver = []
		self.fa=[]
		
        material = None

		for line in open('object_A','r'):
			values=line.split()
			if not values:continue
			if values[0]=='v':
			v=map(float,values[1:4])
			if swapyz:
				v=v[0],v[1],v[2]
				self.Ver.append(v)
            elif values[0]=='f':
            f=map(float,values[1,4])
                self.fa.append(f)