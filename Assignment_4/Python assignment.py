#!/usr/bin/env python
# coding: utf-8

# Write a python program to find the factorial of a number. 

# In[1]:


num = 7
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# Write a python program to find whether a number is prime or composite. 

# In[11]:


num= int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither prime NOR composite number")
else:
    print(num, "is NOT a prime number it is a COMPOSITE number")


# Write a python program to check whether a given string is palindrome or not. 

# In[13]:


my_str = 'NBN'
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


# Write a Python program to get the third side of right-angled triangle from two given sides.

# In[ ]:


import math

a = float(input("Enter base: "))
b = float(input("Enter height: "))
c = math.sqrt(a ** 2 + b ** 2)
print("Hypotenuse =", c)


#  Write a python program to print the frequency of each of the characters present in a given string

# In[2]:


string=input("Enter the string: ")
char=input("Please enter the char to find frequency of character\n")
count=0
for i in range(len(string)):
    if(string[i]==char):
        count=count+1
print("The frequency of the ",char,"in the string is: ",count)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




