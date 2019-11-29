name = ['张三', '李四', 'john', 'lily', 11]
# 打印整个 list
print(name)
# 打印
print(name[0])
print(name[0:2])
print(name[2])
name[1] = 'daye'
print(name)
name.append(101)
print(name)
name.remove(name[0])
print(name[0])
name.reverse()
print(name)
name.append('daf')
print(name)
del name[1]
print(name)
name.pop(1)
print(name)
len(name)
name = name * 4

print(name)
try:
    name.sort()
except:
    print('排序报错了')
else:
    print('排序完成')
print(name)
print(11)
name = ['11', '78', '00', '22', '33', '00']
name.sort()
print(name)
for n in name:
    print(n, '    ', end='')
print(min(name))
print(max(name))
print(name.index('11'))
print(name.count('00'))
list = [[11,22],[33],[22,44,55]]
print(list)
list.sort()
print(list)
list.insert(0,[11])
list.__setitem__(0,[22,88])
print(list)
print([22,88] in list)
