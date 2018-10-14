"""Class of Vectors"""

import math as m

class Vectors(object):

    def __init__(self, vector):
        self.x=vector[0]
        self.y=vector[1]
        self.z=vector[2]
        self.mag=m.sqrt(float(vector[0])**2+float(vector[1])**2+float(vector[2])**2)

    def dot_prod(self,vector_2):
        #get components of vector_2
        comp_1=vector_2[0]
        comp_2=vector_2[1]
        comp_3=vector_2[2]

        return float(float(comp_1)*float(self.x)+float(comp_2)*float(self.y)+float(comp_3)*float(self.z))

    def sum(self,vector_2):

        comp_1=vector_2[0]
        comp_2=vector_2[1]
        comp_3=vector_2[2]

        return [float(comp_1)+float(self.x),float(comp_2)+float(self.y),float(comp_3)+float(self.z)]

    def cross(self,vector_2):
        #get components of vector 2:
        comp_1=vector_2[0]
        comp_2=vector_2[1]
        comp_3=vector_2[2]

        #get components of cross product of self with vector_2:
        cross_1=float(self.y)*float(comp_3)-float(self.z)*float(comp_2)
        cross_2=-float(self.x)*float(comp_3)+float(self.z)*float(comp_1)
        cross_3=float(self.x)*float(comp_2)-float(self.y)*float(comp_1)

        #write cross product vector as a list:
        new_vector=[cross_1,cross_2,cross_3]

        return new_vector
