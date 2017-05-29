# this file for testing some functions for me just 

# f=open('object_B.obj','r')
# print(f.name)
# f.close() 
# with open('object_A.obj','r') as f:
# 	f_inside=f.read()
# 	print(f_inside)
import pywavefront
    from pyglet.gl import *

meshes = pywavefront.Wavefront('object_A.obj')
meshes.draw()