#encoding=utf-8
class Animal:

    def run(self):
        print "Animal can run!"

#Cat子类继承Animal父类
class Cat(Animal):

    def __init__(self):
        print "This is a Cat"

#Dog子类继承Animal父类
class Dog(Animal):

    def __init__(self):
        print "This is a Dog"

#调用父类的方法
cat = Cat()
cat.run()

#调用父类的方法
dog = Dog()
dog.run()


###############################################
class oldClass:

    def __init__(self):
        print "这是一个经典类"

class newClass(object):

    def __init__(self):
        print "这是一个新式类"





#多重继承寻找方法
class D:

    def run(self):
        print "This is class D's run method."

class A(D):

    def run(self):
        print "This is class A's run method."

class B(D):

    def run(self):
        print "This is class B's run method."

class C(A, B):

    def run(self):
        print "This is class C's run method."

c = C()
c.run()

############多态
class F1:
    pass


class S1(F1):
    def show(self):
        print 'S1.show'


class S2(F1):
    def show(self):
        print 'S2.show'


# 由于在Java或C#中定义函数参数时，必须指定参数的类型
# 为了让Func函数既可以执行S1对象的show方法，又可以执行S2对象的show方法，所以，定义了一个S1和S2类的父类
# 而实际传入的参数是：S1对象和S2对象


def Func(F1 obj):
    # """Func函数需要接收一个F1类型或者F1子类的类型"""
    print obj.show()

s1_obj = S1()
Func(s1_obj)  # 在Func函数中传入S1类的对象 s1_obj，执行 S1 的show方法，结果：S1.show

s2_obj = S2()
Func(s2_obj)  # 在Func函数中传入Ss类的对象 ss_obj，执行 Ss 的show方法，结果：S2.show
