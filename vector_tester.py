from vector_class import Vectors
import math as m
import random

def main():
    #create three random vectors whose components can be any real number in the range (-100,100):
    v_1=[random.uniform(-100,100) for i in range(3)]
    v_2=[random.uniform(-100,100) for i in range(3)]
    v_3=[random.uniform(-100,100) for i in range(3)]

    #print these random vectors:
    print("The first vector is:"+str(v_1))
    print("The first vector is:"+str(v_2))
    print("The first vector is:"+str(v_3))

    #Instantiate the three random vectors as instances of the class Vectors
    instance_vector_1=Vectors(v_1)
    instance_vector_2=Vectors(v_2)
    instance_vector_3=Vectors(v_3)

    #Use the class property mag to print the vector's magnitudes
    print("the magnitude of the first vector is:"+str(instance_vector_1.mag))
    print("the magnitude of the second vector is:"+str(instance_vector_2.mag))
    print("the magnitude of the third vector is:"+str(instance_vector_3.mag))

    #use the method dot_prod() to print the dot product of the first random vector with the second
    print("the dot product of the first vector with the second is:"+str(instance_vector_1.dot_prod(v_2)))

    #utilise the sum() method
    print("the sum of the first vector with the second is:"+str(instance_vector_1.sum(v_2)))

    #utilise the cross() method to get the cross product of the first vector with the second
    print("the cross product of the first vector with the second is:"+str(instance_vector_1.cross(v_2)))

    """check whether v_1 cross (v_2 cross v_3) equals (v_1 cross v_2) cross v_3:"""

    #work out the bracketed cross products
    v_1crossv_2=instance_vector_1.cross(v_2)
    v_2crossv_3=instance_vector_2.cross(v_3)

    #instantiate v_1crossv_2 as an instance of Vectors:
    instance_v1_v2=Vectors(v_1crossv_2)

    #test whether the claim is true
    if instance_vector_1.cross(v_2crossv_3)==instance_v1_v2.cross(v_3):
        print("True")
    else:
        print("False")

    """Check whether v_1 cross v_2 equals -v_2 cross v_1"""

    print("cross product of first vector with second:"+str(instance_vector_1.cross(v_2)))
    print("cross product of second vector with first:"+str(instance_vector_2.cross(v_1))) 



main()
