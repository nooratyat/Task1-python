# open files for reading 
# this file for testing some functions for me just 

# f=open('object_B.obj','r')
# print(f.name)
# f.close() 
# with open('object_A.obj','r') as f:
# 	f_inside=f.read()
# 	print(f_inside)
# ////////////////////////////////////////
# import pywavefront
#     from pyglet.gl import *

# meshes = pywavefront.Wavefront('object_A.obj')
# meshes.draw()
# ///////////////////////

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