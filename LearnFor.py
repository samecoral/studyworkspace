#学习for循环
for letter in '白日依山尽':
    print(letter,end='')
    print(letter,end='  ')
dict1 = {"name":"john","age":18,"sex":'girl'}
for d in dict1:
    print(d)
for i  in range(1000):
    print(i)
for i in range(40,99,10):
    print(i)
sum = 0
for i in range(1000):
    sum+=i
    if(sum>1000):
        print(i)
        break
print(sum)
print('--------------------------------------------------------------')
for i in  range(1,10):
    for j in range(1,i+1):
        s = i*j
        print('{}×{}={}'.format(j,i,s),end=' ')
    print('')
print('--------------------------------------------------------------')
for i in range(9,0,-1):
    for j in range(9,i-1,-1):
        print('{}×{}={}'.format(i,j,i*j),end=' ')
    print()

print('--------------------------------------------------------------')
for i in range(9,0,-1):
    for j in range(i,0,-1):
        print('{}×{}={}'.format(i,j,i*j),end=' ')
    print()
