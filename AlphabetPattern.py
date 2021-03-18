#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This Line for to take user input
n = int(input("Enter User Input"))

#this line for store character ASCII value 
alpha = 65;

#This for loop print rows
for i in range(0,n):
    
    #This for loop print columns
    for j in range(0,i+1):
        print(chr(alpha)+' ',end="")
        alpha+=1
    
    print("\r")


# In[ ]:




