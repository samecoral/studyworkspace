#learn if else elsif
import  random
a = random.randrange(0,1000)
print(a)
if(a%2==0):
    print("数字"+str(a)+"是偶数")
else:
    print("数字",a,'是奇数')
while True:
    score = int(input())
    if(score<60 and score>=0):
        print("成绩不及格")
    elif (score>=60 and score<70):
        print('成绩及格')
    elif (score>=70 and score<90):
        print('成绩良')
    elif (score>=90 and score<100 ):
        print('成绩优')
    elif (score==100):
        print('满分')
    else:
        print('超过输入成绩的范围')






