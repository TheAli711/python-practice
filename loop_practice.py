#!/usr/bin/env python
# coding: utf-8

# # Question 1

# ## Write a program that uses a loop to display the characters for each ASCII code 32 through 127. Display 16 characters on each line with one space between characters.

# In[6]:


for i in range(32,128, 16):
    for x in range(i, i+16, 1):
        print(chr(x), end=" ")
    print("")


# # Question 2
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


# # Question 3

# ## Write a program that asks the user for the speed of a vehicle (in miles per hour) and how many hours it has traveled. It should then use a loop to display the total distance traveled at the end of each hour of that time period.
# ### Input Validation: Do not accept a negative number for speed and do not accept any value less than one for time traveled

# In[7]:


speed = -1
while speed < 0:
    speed = int(input("What is the speed of the vehicle in mph? "))

distance = 0
while distance < 1:
    distance = int(input("How many hours has it traveled? "))

print("------------------------------")
print("Hour Distance Travelled")
print("------------------------------")
for i in range(1,distance+1):
    print(i , "\t\t\t" , speed*i)
print("------------------------------")


# # Question 4

# ## You were asked to write a program that converts a Celsius temperature to Fahrenheit and Kelvin . Modify that program so it uses a loop to display a table of the Celsius temperatures from 0 to 20 and their Kelvin and Fahrenheit equivalents.

# In[14]:


print("-------------------------------------------")
print("Celsius", "\t", "Fahrenheit", "\t", "Kelvin")
print("-------------------------------------------")
for i in range(20):
    print(i , "\t\t" ,  i*9/5 , "\t\t" , i+273.15)
print("-------------------------------------------")


# # Question 5

# ## Write a program that displays a table of speeds in kilometers per hour with their values converted to miles per hour. The table should display the speeds from 60 kilometers per hour through 130 kilometers per hour, in increments of 5 kilometers per hour

# In[15]:


print("-------------------------------------------")
print("KPH", "\t\t", "MPH")
print("-------------------------------------------")
for i in range(60,135, 5):
    print(i, "\t\t", i*0.6214)


# # Question 6

# ## Write a program that calculates how much a person earns in a month if the salary is one penny the first day, two pennies the second day, four pennies the third day, and so on with the daily pay doubling each day the employee works. The program should ask the user for the number of days the employee worked during the month and should display a table showing how much the salary was for each day worked, as well as the total pay earned for the month. The output should be displayed in dollars with two decimal points, not in pennies.
# ### Input Validation: Do not accept a number less than 1 or more than 31 for the number of days worked.

# In[34]:


days = 0
salary = 1
while (1 > days or days > 31):
    days = int(input("Number of days worked: "))
    
print("----------------------------------")
print("Day # \t\t\t Pay")
print("----------------------------------")
print("1 \t\t\t 0.01")
for i in range(2,days+1):
    salary = salary + salary
    print(i, "\t\t\t", salary/100)
print("----------------------------------")
print("Total Salary for this month: \t", salary/100)
print("----------------------------------")

