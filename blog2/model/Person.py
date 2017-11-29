#定义类
class Person:

    #构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        print self.name
        print self.age

#封装对象
xiaoMing = Person("xiaoming", 16)
xiaoGang = Person("xiaogang", 15)

#调用被封装的内容
print xiaoMing.name
print xiaoMing.age

print xiaoGang.name
print xiaoGang.age

print xiaoMing.detail()
print xiaoGang.detail()