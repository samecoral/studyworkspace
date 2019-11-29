#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#learn dict
dict1 = {'username':"john",'sex':"男","age":18}
print(dict1)
print(dict1['username'])
print(dict1.keys())
print(dict1.items())
print(dict1.values())
print(type(dict1.values()))
dict1['11']='2'
print(dict1)
for i in dict1.items():
    print(i[0])
for j in dict1.values():
    print(j)
