#!/usr/bin/env python
# coding: utf-8

# In[2]:


#This Line for to take user input
n = int(input("Enter User Input"))

#This for loop print rows
for i in range(1,n+1):
    
    #This for loop print columns
    for j in range(1,n+1):
        
        #This if will check condition is matiching or not 
        if j<=(n-i):
            print(" ",end="")
        else:
            print("*",end="")
    
    print("\r")


# In[ ]:




