# from OpenGL.GL import *
import numpy as np

class ObjLoader:
	
	def __init__(self):
	
		self.vert1 = []
		# self.face = []
		self.norm = []

		self.vert_index = []
		self.norm_index = []

		self.model=[]

	def load_model(self, file):
	    for line in open(file,'r'):
			if line.startwith('#'):continue
			values=line.split()
		    if not values:continue

			if values[0] == 'v':
			   self.vert1.append(values[1:4])
			if values[0] == 'vn':
			   self.norm.append(values[1:4])
			if values[0] == 'f':
				face_i = []
				norm_i = []
				for v in values[1:4]:
					w = v.split('/')
					face_i.append(int(w[0])-1)
					norm_i.append(int(w[1])-1)
				self.vert_index.append(face_i)
				self.norm_index.append(norm_i)	
	    self.vert_index = [y for x in self.vert_index for y in x]
	    self.norm_index = [y for x in self.norm_index for y in x]
				
		for i in self.vert_index:
			self.model.extend(self.vert1[i])
								

		for i in self.norm_index:
			self.model.extend(self.norm[i])
				
        self.model = np.array(self.model, dtype='float32')



                    obj=ObjLoader()
                    obj.load_model("object_A.obj")+ obj.load_model("object_B.obj")
                   




# with open("object_A.obj", "wb") as outfile:
#     for f in read_files:
#         with open(f, "rb") as infile:
#             outfile.write(infile.read())

