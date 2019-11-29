#learn Tuple
tuple1=(11,22,'2121','333')
print(tuple1)
print(tuple1.count('11'))
print(tuple1[0])
print(tuple1[1:2])
print(tuple1.__contains__('11'))
tuple2 = ()
tuple2=('11',)
print(tuple2)
tuple2 = tuple2.__add__(('11',))
print(tuple2)
list1 = [79,85]
tuple2 = tuple2.__add__((list1,))
print(tuple2)
tuple3=(11,99,'08',list1)
print(tuple3)
list1[0]=12

print(tuple2)
print(tuple3)
del tuple2
list2 = ['hah','11','qwe']
tuple4 = tuple(list2)
print(tuple4)
