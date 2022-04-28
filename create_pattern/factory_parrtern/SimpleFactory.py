'''
@author = xiaolin.wang
@description:
    简单工厂
        统一使用一个类作为对外接口，根据参数的不同，去选择实例化不同的类

    简单工厂使用场景：
    已经确定有多少具体的类，不会再增加的情况下使用。
'''

class TechnicalBooks(object):
    def publish(self):
        return "Python-Book"

class LiteraryBooks(object):
    def publish(self):
        return "Black Hole Book"

class SimpleFactory(object):

    @staticmethod
    def publish_book(name):
        if name == 'technical':
            return TechnicalBooks()
        elif name == 'literary':
            return LiteraryBooks()
if __name__ == "__main__":
    it_books = TechnicalBooks()
    ly_books = LiteraryBooks()

    it_books2 = SimpleFactory.publish_book('technical')
    ly_books2 = SimpleFactory.publish_book('literary')
