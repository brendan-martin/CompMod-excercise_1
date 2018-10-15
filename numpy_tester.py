"""Test Vector identities using numpy"""


import numpy as np
import random

def main():
    #create three random arrays called v_1, v_2, v_3 whose entries are random real numbers in range (-100,100)
    v_1=np.array([random.uniform(-100,100) for i in range(3)])
    v_2=np.array([random.uniform(-100,100) for i in range(3)])
    v_3=np.array([random.uniform(-100,100) for i in range(3)])

    #print the vectors to the terminal:
    print("the first vector is:"+str(v_1))
    print("the first second is:"+str(v_2))
    print("the first third is:"+str(v_3))
    #print the norms of each vector to the terminal
    print("the norm of the first vector is:"+str(np.linalg.norm(v_1)))
    print("the norm of the second vector is:"+str(np.linalg.norm(v_2)))
    print("the norm of the third vector is:"+str(np.linalg.norm(v_3)))

    #print the sum of the first two vectors using the operator overloading of numpy
    sum=v_1+v_2
    print("the sum of the first two vectors is:"+str(sum))

    #print the dot product of the first two vectors using np.inner()
    dot_prod=np.inner(v_1,v_2)
    print("the dot product of the first and second vectors is:"+str(dot_prod))

    #calculate cross product of first and second vectors using np.cross
    cross_prod=np.cross(v_1,v_2)
    print("the cross product of the first and second vectors is:"+str(cross_prod))

    


main()
