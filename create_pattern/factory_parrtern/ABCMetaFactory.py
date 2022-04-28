'''
@author = xiaolin.wang
@description:
    抽象工厂

    抽象工厂的使用场景：
        当多个产品(步骤)集合在一起，组成产品族时。
        对于一个产品族，如果只想显示接口而不是实现时。
'''
import abc


# 印刷书籍
class PrintingTechnicalBooks(object):
    """印刷技术书籍"""

    def printing(self):
        return "Print-Python-Book"


class PrintingLiteraryBooks(object):
    """印刷文学书籍"""

    def printing(self):
        return "Print Black Hole Book"


# 出版书籍
class TechnicalBooks(object):
    """出版技术书籍"""

    def publish(self):
        return "Python-Book"


class LiteraryBooks(object):
    """出版文学书籍"""

    def publish(self):
        return "Black Hole Book"


# 抽象工厂：先定义抽象类，然后每种类型的书籍都有自己对于的工厂
class AbstractFactory(metaclass=abc.ABCMeta):
    """抽象工厂"""

    @abc.abstractmethod
    def print_book(self):
        pass

    @abc.abstractmethod
    def publish_book(self):
        pass


class TechnicalFactory(AbstractFactory):
    """技术书籍工厂"""

    def print_book(self):
        return PrintingTechnicalBooks()

    def publish_book(self):
        return TechnicalBooks()


class LiteraryFactory(AbstractFactory):
    """文学书籍工厂"""

    def print_book(self):
        return PrintingLiteraryBooks()

    def publish_book(self):
        return LiteraryBooks()


if __name__ == "__main__":
    # 实例化工厂对象
    it = TechnicalFactory()
    ly = LiteraryFactory()

    # 印刷书籍
    it_print = it.print_book()
    ly_print = ly.print_book()
    # 出版书籍
    it_publish = it.publish_book()
    ly_publish = ly.publish_book()
