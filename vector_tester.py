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
    print("The second vector is:"+str(v_2))
    print("The third vector is:"+str(v_3))

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


    #Work out the cross products of the three vectors for use in verifying the vector identities
    v_1crossv_2=instance_vector_1.cross(v_2)
    v_2crossv_3=instance_vector_2.cross(v_3)
    v_1crossv_3=instance_vector_1.cross(v_3)

    #instantiate v_1crossv_2 as an instance of Vectors:
    instance_v1_v2=Vectors(v_1crossv_2)


    """check whether the BAC-CAB rule is true"""
    #work out LHS
    v_lhs=instance_vector_1.cross(v_1crossv_3)

    #work out the dot products on the RHS and call them dot_1 and dot_2
    dot_1=instance_vector_1.dot_prod(v_2)
    dot_2=instance_vector_1.dot_prod(v_3)

    #work out (separately) the two terms on RHS using the "scalar_multiple" method in vectors
    term_1=instance_vector_2.scalar_multiple(dot_1)
    term_2=instance_vector_3.scalar_multiple(dot_2)

    #instantiate term_1 as an instance of Vectors
    instance_term1=Vectors(term_1)

    #work out RHS using "sum" method of vectors
    v_rhs=instance_term1.sum(term_2)

    #print the LHS and RHS to the terminal
    print("the left hand side of the BAC-CAB identity is:"+str(v_lhs))
    print("the right hand side of the BAC-CAB identity is:"+str(v_rhs))

    #instantiate v_lhs
    instance_lhs=Vectors(v_lhs)

    #check whether the identity holds by using the "same" method
    print("Are the vecots on the left hand and right hand side of the BAC-CAB identity the same?"+str(instance_lhs.same(v_rhs)))

    """Check whether v_1 cross v_2 equals -v_2 cross v_1"""
    #work out the LHS and the RHS and call them v_a and v_b respectively
    v_a=instance_vector_1.cross(v_2)
    v_b=instance_vector_2.cross(v_1)

    print("cross product of first vector with second:"+str(v_a))
    print("cross product of second vector with first:"+str(v_b))

    #Instantiate v_a as an instance of Vectors so that we can us the "same" method
    instance_v_a=Vectors(v_a)
    print("Are these vectors the same?"+str(instance_v_a.same(v_b)))


    """Check whether v_1 cross (v_2+v_3) equals (v_1 cross v_2)+(v_1 cross v_3)"""

    #work out v_2+v_3
    v_c=instance_vector_2.sum(v_3)

    #work out LHS
    v_left=instance_vector_1.cross(v_c)

    #work out RHS
    v_right=instance_v1_v2.sum(v_1crossv_3)

    #print the LHS and RHS to the terminal
    print("The first vector crossed with the sum of the other two is:"+str(v_left))
    print("The sum of the first vector crossed with the second and the first vector crossed with the third is:"+str(v_right))

    #instantiate v_left as an instance of the Vectors class
    instance_left=Vectors(v_left)

    #use the "same"method to work out whether v_left equals v_right
    print("Are these vectors the same?"+" "+str(instance_left.same(v_right)))


main()
