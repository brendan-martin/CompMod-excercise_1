import numpy as np

side_length=input("the length of each side of the cube is:")

length_vector=np.array([float(side_length),float(side_length),float(side_length)])


#work out components of given vector
comp1=input("The first component of the position vector is:")
comp2=input("The second component of the position vector is:")
comp3=input("The third component of the position vector is:")

given_vector=np.array([float(comp1),float(comp2),float(comp3)])

#work out the replica vector
replica=np.mod(given_vector,length_vector)

print("The equivalent point in the origional box is given by:"+str(replica))
