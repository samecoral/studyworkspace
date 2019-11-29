#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
author caohs
学习私有方法
"""


class UserInfo(object):
    "fasdfafafdasfsfddasfasf"

    def __init__(self, name, age, account):
        """dafafdfadfad"""
        self.name = name;
        self.age = age;
        self.__account = account

    def get_accout(self):
        """dfadfa"""
        return self.__account


if (__name__ == '__main__'):
    u = UserInfo('hh', 11, 1215.2)
    print(dir(u))
    print(u.__dict__)
    print(u.__dir__)
    print(u.__doc__)
    print(u.__class__)
    print(u.get_accout())
    print(u._UserInfo__account)


class User(object):
    def create_user(self):
        pass

    def _del_user(self):
        pass

    def __pk__(self):
        pass


#import  sys
#print(sys.path)
#print(sys.version_info)

from sys import *
print(path)
print(version_info)
