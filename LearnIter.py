# learn iterator
str1 = '我家那位傻屌天天只知道看电视，逛淘宝'
inter1 = iter(str1)
print(inter1)
for i in inter1:
    print(i, end=' ')



print("------------------------------")
inter2 = iter((1,2,3,7,9))
while True:
    try:
        print(next(inter2))
    except StopIteration:
        break


# 反向迭代
list1 = [1,2,3,4,5,6]
iter2 = iter(list1)
print('正向迭代 ')
for i in iter2:
    print(i,end=' ')
print('\n反向迭代')
for i in iter(reversed(list1)):
    print(i,end=' ')
name=['zhangsan','lishi','lily','john']
age = [19,21,23,21]
for n ,a in  zip(iter(name),iter(age)):
    print(n,end=' ')
    print(a,end=' ')
    print()
dict1 = dict(zip(iter(name), iter(age)))
print(dict1)