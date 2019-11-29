class LearnClass(object):
    a, b, c = '1', 2, ["zhangsan", "lisi", "王五"]

    def fun1(self):
        print(' 我是谁，我是'+LearnClass.a)



    @classmethod
    def fun2(cls,age,b):
        print('类方法取值'+cls.a+'获取外部值'+str(age))
        cls.b = b


LearnClass.fun1(LearnClass)
LearnClass.fun2(18,99)
print(LearnClass.b)
LearnClass.a = '10'
LearnClass.fun1(1)


class cl_b(object):
    var1 = '1'
    def fun(self):
        return self.var1



Class1 = cl_b()
Class1.var1 = 10
print(Class1.var1)
Class2 = cl_b()
print(Class2.var1)
