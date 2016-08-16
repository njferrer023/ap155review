
# coding: utf-8

# In[1]:

from randnumber import randnum
from __future__ import division
from numpy import random

def main():
    print "Exercise 8.1"

    #partA
    print "Part A: The two random numbers are ", randnum(), "and ", randnum()



    print "Part B: "

    numlist = []
    count = 0.0
    N = int(1e6+1)
    for n in xrange(0,N):
        num1 = randnum()
        num2 = randnum()
        numlist.append(num1)
        numlist.append(num2)
        if num1 == 6 and num2 ==6:
            count +=1
    fraction = count/1e6
    print fraction


if __name__ == "__main__":
    # execute only if run as a script
    main()


# In[ ]:



