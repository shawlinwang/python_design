'''
@author = xiaolin.wang
@description:
    工厂方法:每个工厂就只负责生产自己的产品，避免了在新增产品时需要修改工厂的代码，遵循了"开闭原则"，如果需要新增产品时，只需要增加相应的工厂即可。

    工厂方法的使用场景：
        当系统中拥有的子类很多，并且以后可能还需要不断拓展增加不同的子类时。
        当设计系统时，还不能明确具体有哪些类时。
'''

import abc

class TechnicalBooks(object):
    def publish(self):
        return "Python-Book"

class LiteraryBooks(object):
    def publish(self):
        return "Black Hole Book"

# 抽象工厂：先定义抽象类，然后每种类型的书籍都有自己对于的工厂
class AbstractFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def publish_book(self):
        pass

class TechnicalFactory(AbstractFactory):

    def publish_book(self):
        return TechnicalBooks()

class LiteraryFactory(AbstractFactory):

    def publish_book(self):
        return LiteraryBooks()

if __name__ == "__main__":
    it_books2 = TechnicalFactory().publish_book()
    ly_books2 = LiteraryFactory().publish_book()
