
# coding: utf-8

# In[1]:

from height import h

if __name__ == "__main__":
    # execute only if run as a script

    #Exercise 1.1: Altitude of a satellite
    print "Exercise 1.1"

    #partA

    #partB

    print "Part B:"
    print "Desired value of time T in seconds: "
    T = 8
    print "The altitude above the Earth's surface of the satellite is ", h(T) , "meters"

    #partC
    #Calculate the height if it orbits once a day
    x = 86400 #one day in seconds
    print "Part C.1: The altitude of the satellite that orbits the Earth once a day is ", h(x), "meters."
    #Calculate the height if it orbits once every 90 mins
    y = 5400
    print "Part C.2: The altitude of the satellite that orbits the Earth once every 90 minutes is ", h(y), "meters."
    #Calculate the height if it orbits once every 45 mins
    z = 2700
    print "Part C.3: The altitude of the satellite that orbits the Earth once a day is ", h(z), "meters."


    #partD
    T1 = 23.93*60*60 #23.93 hrs in seconds
    print "The altitude of the satellite that orbits the Earth once every for 23.93 hrs is ", h(T1), "meters."


    T2 = 24*60*60 #24 hrs in seconds
    print "Part D:"
    print "The altitude of the satellite that orbits the Earth once every 24 hours is", h(T2), "meters."



# In[ ]:




# In[ ]:



