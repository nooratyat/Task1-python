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
import numpy as np

class ObjLoader:
	
	def __init__(self, arg):
	
		self.vert = []
		self.face = []
		self.model=[]
	def load-model(self,file):
			for line in open(file,'r'):
				if line.startwith('#'):continue
				values=line.split()
			    if not values:continue

			    if values[0] == 'v':
			    	self.vert.append(values[1:4])
			    if values[0] == 'f':
			        self.face.append(values[1:4])	


                    self.model = np.array(self.model, dtype='float32')



                    obj=ObjLoader()
                    obj.load-model("object_A.obj")
                    obj.load-model("object_B.obj")






