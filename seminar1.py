#Munkhtsetseg_DBP221_452
#1
list1=['python', 'php', 'java']
print(list1[0])
print(list1[1])
print(list1[2])
#2
lista= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e=0
t=0
while(e<len(lista)):
    t=t+lista[e]
    e+=1
print(t)  
#3
def multiplyList(list) :
    t=1
    for x in list:
         t = t * x
    return t
list1=[1, 2, 3, 4, 5]
print(multiplyList(list1))
#4
list2=[1, 2, 3, 4, 5]
print(list2[2]*list2[-1])
#5
list2=['1', '2', '3', '4', '5]
print(max(list2), min(list2))
#6
def match_words(words):
  c = 0
  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      c += 1
  return c

print(match_words(['abca', 'aa','dgaga','21', 'aba', '1221']))
#7
list3=['abdba', 'abcd', '121', '121', 'abcd']
x=set(list3)
y=list(x)
print(y)
#8
list = []
if len(list):
    print('The list is not empty')
else:
    print('The list is empty')
#9
list4=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
del list4[3]
del list4[4]
del list4[5]
print(list4)
#10
tuple1=(1,2,3,4,5,6,7,8,9,10)
print(tuple1)
#11
tuple1=('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus')
tuple1=tuple1+('Neptune',)
#12
tuple1=(1,2,3,4,5,6,7,8,9,10)
print(tuple1[1], tuple1[-2])
#13
too = ('1','2','3','4','5','6')
too1= input('toogoo oruul')
if too1 in too:
    print('baina')
else:
    print('baihgui')
#14
e=0
tuple1=(1,2,3,4,5,6,7,8,9,10)
for e in tuple1:
    print(e)
#15
set1={'1','2','3','4','5'}
set2={'6','7','8','9','10'}
set3=set.union(set1, set2)
print(set3)
#16
set1={'1','2','3','4','5'}
set2={'6','7','3','2','1'}
k = set(set1)
i = k.intersection(set2)
t = set(i)
print(t)
#17
set1={'1','2','3','4','5'}
print(len(set1))
#18
set1 = {1,2,3,4,5,6,7,8,9,0}
set2 = {2,4,6,8,0}
set1 = set1.difference(set2)
print(set1)
#19
set1={'1','2','3','4','5'}
set1.clear()
print(set1)
#20
set1={'1','2','3','4','5'}
del set1
print(set1)
#21
dict1={'1':'10','2':'20','3':'30'}
print (sort_dict_by_value(dict1))
print(sort_dict_by_value(dict1, True))
#22
d = {"key1": 2, "key2": 3}
if "key2" in d:
    print("yes")
else:
    print("no")
#23
dict1={'1':'10','2':'20','3':'30'}
if '20' in dict1.values():
    print('20 is in dictionary')
else:
    print("No")
# 24
dict1={'1':'10','2':'20','3':'30'}
for x in dict1:
  print(x, dict1[x])
#25
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
dict1={'1':'10','2':'20','3':'30'}
dict2={'a':'11','b':'22','c':'33'}
dict3 = Merge(dict1, dict2)
print(dict3)
#26
dict1 ={'1':10,'2':20,'3':30}
v = dict1.values()
t = sum(v)
print(t)
