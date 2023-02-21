#!/usr/bin/env python
# coding: utf-8

# In[64]:


def print_times(List) :

    List = [5, 6, -1, 2, 4, -2, -10, 7]
    
    product = 1
    for x in List:
         product = product * x
    return product
     
print("All numbers: " + str(List))
print("Product:",print_times(List))


# In[37]:


def print_f(x):
    x()
    
def print_rep(x):
    print_twice(x)

def print_plus():
    print('+','- '*4, '+','- '*4, '+','- '*4, end= '')
    print('+','- '*4,'+')

def print_strt():
    for i in range(4):
        print('|         ', '|         ', '|         ', end= '')
        print('|         ','|')

def print_twice(print_rep):
    print_plus()
    print_strt()
    
def print_rest():
        for i in range(3):
            print_twice(print_rep)
    
print_twice(print_rep)
print_rest()
print_plus()

