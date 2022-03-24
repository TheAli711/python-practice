#!/usr/bin/env python
# coding: utf-8

# # Question1

# ## Write a program that uses a loop to display the characters for each ASCII code 32 through 127. Display 16 characters on each line with one space between characters.

# In[6]:


for i in range(32,128, 16):
    for x in range(i, i+16, 1):
        print(chr(x), end=" ")
    print("")


# # Question2
# 

# ## Write a program that asks the user for a positive integer value. The program should use a loop to get the sum of all the integers from 1 up to the number entered. For example, if the user enters 50, the loop will find the sum of 1, 2, 3, 4, ... 50.
# ### Input Validation: Do not accept an input that is less than 1.

# In[12]:


x = int(input("Enter Positive Number: "))
y = 0;
if(x < 1):
    print("Wrong Input")
else:
    for i in range(1,x):
        y += i
y += x

print(y)


# In[ ]:




