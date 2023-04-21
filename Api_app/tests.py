from django.test import TestCase

# Create your tests here.
list = ['第一条','第二条','第三条']
print(list[::-1][0:2]) #[::-1]固定写法，倒序作用。先倒序再切片区前两个元素，达到了去最后两个最新的数据的目的

def a(**b):
    print(b)
a(c=1,d=2)

def fun(i,message=''):
    print(i,message)

fun(2,3)

try:
    print(k)
except:
    print('okk')


#字典
d = {}
d['a'] = 1
print(d['a'])

import json
A = {"a":1,"b":2}

B = json.dumps(A) #字典转成json
print(B,type(B))
print(A,type(A))
print(A['b'])

c = json.loads(B)  #json转成字典
print(c,type(c))


a1 = "{'a':1}"
a2 = json.loads(a1)
print(a2)