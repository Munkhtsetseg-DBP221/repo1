# In[12]:


#Munkhtsetseg_452
#1
n=int(input())
for i in range(1, n+1):
    print("*"*i)


# In[33]:


#2
def input_(n):
    for i in range(0,n):
        for j in range (0,i+1):
            print("*", end=" ")
        print("\r")
input_(6)


# In[28]:


#3
students = {'Bat': 18, 'Oyun': 22, 'Dulam': 21, 'Suren': 20}
Keymax=max(students, key=students.get)
Keymin=min(students, key=students.get)
print(Keymax, Keymin)


# In[38]:


students = {'Bat': 18, 'Oyun': 22, 'Dulam': 21, 'Suren': 20}
print(max(students, key=students.get),min(students, key=students.get))


# In[25]:


import numpy as np
x=np.arange(1,1000)
n=x[(x%3==0)|(x%7==0)]
print(n[:1000])
print(n.sum())


