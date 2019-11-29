#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#learn set
set1 = set([11,44,22,88,65])
print(set1)
set1.add(88)
print(set1)
set1.add(12)
print(set1)
set1.remove(44)
print(set1)
set2 = set([11,44,88,99])
set3 = set2 & set1
print(set3)
set4 = set2|set1
print(set4)
print(set2-set1)
print(set1-set2)

