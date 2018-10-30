from vector_class import Vectors
import math as m


def main():
    #ask user for components of the first vector
    component_1=input("The first component of the vector is:")
    component_2=input("The second component of the vector is:")
    component_3=input("The third component of the vector is:")

    vector_1=[component_1,component_2,component_3]
    print("the first vector is"+str(vector_1))

    #ask user for components of the second vector
    component2_1=input("The first component of the second vector is:")
    component2_2=input("The second component of the second vector is:")
    component2_3=input("The third component of the second vector is:")

    vector_2=[component2_1,component2_2,component2_3]
    print("the second vector is"+str(vector_2))

    #ask user for a scalar scalar multiple, c
    c=input("my scalar multiple is:")

    #initialise the first vector as an instance of the class Vectors
    instance_vector=Vectors(vector_1)

    #use mag property of vectors to compute the magnitude of the first vector
    magnitude=instance_vector.mag
    print("the magnitude of the first vector is:"+str(magnitude))

    #use mag2 property of vectors to compute the squared magnitude of the first vector
    magnitude2=instance_vector.mag2
    print("the squared magnitude of the first vector is:"+str(magnitude2))

    #use class method to compute dot product of the two vectors
    dot_product=instance_vector.dot_prod(vector_2)
    print("the dot product of the two vectors is:"+str(dot_product))

    #find scalar multiple of first vector
    multiple=instance_vector.scalar_multiple(c)
    print("the scalar multiple of the first vector is:"+str(multiple))

    #use class method "cross" to compute cross product of the two vectors
    print("the cross product of the two vectors is:"+str(instance_vector.cross(vector_2)))

    #use class method "sum" to add the two vectors
    print("the sum of the two vectors is:"+str(instance_vector.sum(vector_2)))

    #use class method "diff" the subtract the first vector from the second
    print("the second vector minus the first is:"+str(instance_vector.diff(vector_2)))

    #check whether the two vectors are the same
    print("are the two vectors the same?"+str(instance_vector.same(vector_2)))

main()
