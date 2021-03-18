#!/usr/bin/env python
# coding: utf-8

# In[9]:


import sys

prodList = {}

#This line for to ask to user his/her budget and store in budget variable
budget = int(input("Enter Your Budget : "))

#This function to prepare grocery list as per the user requirment  
def prod_list():
    
    #below two line accesing global variable for make the chance in them
    global budget
    global prodList
    
    #Below 3 lines will ask to user product name, quantity and price 
    product = input("\n\nEnter product : ")
    quantity = float(input("Enter Quantity : "))
    price = float(input("Enter Price : "))
    
    #This if is for stop buying the product if budget is less then product price 
    if budget<price:
        print("\n\n Can't By the product ##(because budget left is )",budget,"\n\n")
        return
    
    #this line store bought products and those quantity, price  
    prodList[product] = [quantity,price]
    
    #This line wil detuct the product price from budget one user bought the product
    budget-=price;
    
    #it will print remaining budget
    print("\n\n Amount left : ",budget,"\n\n")
    
    
#The my_exit() function is for to stop program execution after displaying the Grocery List 
#once Shopping completed 
def my_exit():
    
    #if budget is remaning This if will invite the user to buy more things
    if budget != 0:
        print("\n\n Amount left can you buy something.... \n\n")
        
    print("GROCERY LIST is: \n")
    print("Product Name\t Quantity\t Price")
    
    #This for loop will print the grocery list
    for key, val in prodList.items():
        print(key,"\t\t",val[0],"\t\t",val[1])
        print("\n")
        
    #The exit() will terminate the program once Shopping done     
    sys.exit('Shopping Done Successfully!')
    

#This while loop keep running program and ask the shopping deatils until user complete the shopping 
while budget!=0:
    
    #Below two lince the massage for user to select the choice
    print("1.Add an item")
    print("2.Exit")
    
    #This line ask the user choice abd store in choice variable  
    choice = int(input("Enter your choice : "))
    
    #if the user select choice 1 then this if will call the function for grocery list
    if choice == 1:
        prod_list()
    
    #if the user select the choice 2 then this if will call the function for exit the program
    if choice == 2:
        my_exit()
        
        
#if the user given budget is 0 then this if will call my_exit() and terminate the program 
if budget == 0:
    my_exit()


# In[ ]:





# In[ ]:




