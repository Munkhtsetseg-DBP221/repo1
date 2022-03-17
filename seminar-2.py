Munkhtsetseg b20fa1531 
Group 452
# In[1]:


#1
def palindrome(values):
  c = 0
  for value in values:
    if len(value) > 1 and value[0] == value[-1]:
      c += 1
  return c
print(palindrome(['abca', 'aa','dgaga','21', 'aba', '1221']))


# In[9]:


#2
s = "Python language"
l,u = 0,0
for i in s:
    if (i>='a'and i<='z'):
        l=l+1                 
    if (i>='A'and i<='Z'):
        u=u+1   
          
print('Lower case characters: ',l)
print('Upper case characters: ',u)


# In[10]:


#3
def multiplyList(value) :
    t=1
    for x in value:
         t = t * x
    return t
value1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(multiplyList(value1))


# In[2]:


#4
def factorial_(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact
print(factorial_(5))


# In[6]:


#5
def reverse(list):
    list.reverse()
    return list
list1=[1,3,4,6,7]
print(reverse(list1))
    


# In[6]:


#6
def multiplyList(value) :
    t=1
    for x in value:
         t = t + x
    return t
value1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(multiplyList(value1))


# In[12]:


#7
def multiplyList(list) :
    my_final_list = set(list)
    return my_final_list
my_list = [1,1,2,3,2,2,4,5,6,2,1]
print(multiplyList(my_list))


# In[16]:


#8
def maxinum(x, y, z):
    if (x >= y) and (x >= z):
        largest = x
    elif (y >= x) and (y >= z):
        largest = y
    else:
        largest = z
    return largest
x = 10
y = 14
z = 12
print(maximum(x, y, z))







