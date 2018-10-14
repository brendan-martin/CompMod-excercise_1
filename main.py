from vector_class import Vectors
import math as m


def main():

    component_1=input("The first component of the vector is:")
    component_2=input("The second component of the vector is:")
    component_3=input("The third component of the vector is:")

    vector_1=[component_1,component_2,component_3]

    component2_1=input("The first component of the second vector is:")
    component2_2=input("The second component of the second vector is:")
    component2_3=input("The third component of the second vector is:")

    vector_2=[component2_1,component2_2,component2_3]

    instance_vector=Vectors(vector_1)

    magnitude=instance_vector.mag

    print(magnitude)

    dot_product=instance_vector.dot_prod(vector_2)

    print(dot_product)
main()
