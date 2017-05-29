# open files for reading 
# f=open('object_B.obj','r')
# print(f.name)
# f.close() 
# with open('object_A.obj','r') as f:
# 	f_inside=f.read()
# 	print(f_inside)
from mesh import obj 

first = obj.Obj("object_A.obj") 
second= obj.Obj("object_B.obj") 
class OBJ:
	"""docstring for OBJ"""
	def __init__(self, object_A):
		# super(OBJ, self).__init__()
		self.Ver = []
		self.fa=[]

		for line in open('object_A','r'):
			values=line.split()
			if not values:continue
			if values[0]=='v'
			v=map(float,values[1:4])
			if swapyz:
				v=v[0],v[1],v[2]
				self.Ver.append(v)
            if values[0]=='f'
            f=map(float,values[1,4])
                self.fa.append(f)