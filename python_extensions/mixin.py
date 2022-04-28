'''
@author = xiaolin.wang
@description:
    扩展类的功能、插件类
    一般情况下mixin类不写__init__ 方法， minxin类有些属性在minxin中不具备，所以不可以把mixin类进行实例化使用
    mixin类可以直接访问基本类的方法和属性
'''
class Person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("行走")

class StudyMixin:
    def study(self):
        print(self.name + '...在上课学习...')

class Student(Person, StudyMixin):
    def __init__(self, name, age):
        Person.__init__(self, name)
        self.age = age

    def eat(self):
        print(self.name + '...在吃饭...')

if __name__ == "__main__":
    Student('小明', 10).study()
