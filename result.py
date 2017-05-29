# open files for reading 
# f=open('object_B.obj','r')
# print(f.name)
# f.close() 
# with open('object_A.obj','r') as f:
# 	f_inside=f.read()
# 	print(f_inside)
class OBJ:
	"""docstring for OBJ"""
	def __init__(self, object_A):
		# super(OBJ, self).__init__()
		self.V = []
		self.f=[]

		for line in open('object_A','r'):
			values=line.split()
			if not values:continue
			if values[0]=='v'
			v=map(float,values[1:4])
			if swapyz:
				v=v[0],v[1],v[2]
				self.V.append(v)
