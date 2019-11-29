#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class user_lname(object):
    def __new__(cls, *args, **kwargs):
        print("调用了new 方法")
        print(cls)
        print(*args)
        print("**"+str(**kwargs))
        return super(user_lname,cls).__new__(cls);
    def __init__(self,name,age,acc):
        print("调用了初始化方法")
        self.name = name
        self.age = age;
        self.acc = acc;

ul = user_lname('hhhh',19,12.11)





import lname
print(__name__)

