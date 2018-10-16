"""Class of Vectors"""

import math as m

class Vectors(object):

    def __init__(self, vector):
        #the components are internal properties of a  vector
        self.x=vector[0]
        self.y=vector[1]
        self.z=vector[2]
        #create an internal property called mag which is the magnitude of the vector
        self.mag=m.sqrt(float(vector[0])**2+float(vector[1])**2+float(vector[2])**2)
        #create an internal property called mag2 that is the magnitude squared of the vectors
        self.mag2=float(vector[0])**2+float(vector[1])**2+float(vector[2])**2

    #define a method that takes an outside vector and dot products it with the instance vector
    def dot_prod(self,vector_2):
        #get components of vector_2
        comp_1=vector_2[0]
        comp_2=vector_2[1]
        comp_3=vector_2[2]
        #add up the products of the components of each vector
        return float(float(comp_1)*float(self.x)+float(comp_2)*float(self.y)+float(comp_3)*float(self.z))

    #define a method that takes an outside vector and sums it with the instance vector
    def sum(self,vector_2):

        comp_1=vector_2[0]
        comp_2=vector_2[1]
        comp_3=vector_2[2]

        #return a list of the summed components of the two vectors
        return [float(comp_1)+float(self.x),float(comp_2)+float(self.y),float(comp_3)+float(self.z)]

    #define a method that takes an outside vector and subtracts the instance vector from it
    def diff(self,vector_2):

        comp_1=vector_2[0]
        comp_2=vector_2[1]
        comp_3=vector_2[2]

        return [float(comp_1)-float(self.x),float(comp_2)-float(self.y),float(comp_3)-float(self.z)]


    #define a method that takes an outside vector and cross products it with the instance vector
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

    #define a method that takes a scalar c and multiplies each component of self by c
    def scalar_multiple(self,c):
        #get the components of the scalar multiple of the vector and call them n_vi for i=0,1,2
        n_v0=float(c)*float(self.x)
        n_v1=float(c)*float(self.y)
        n_v2=float(c)*float(self.z)

        #return the new components as a list
        return [n_v0,n_v1,n_v2]

    #define a method that checks whether another vector (vector_2) is the same as the instance vector
    def same(self,vector_2):
        if self==vector_2:
            return str("yes, they are the same")
        else:
            return str("no, they are different")
