'''
@author = xiaolin.wang
@description:
    继承实现单例模式
'''
class ParentClass:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'ins'):
            insObject = super(__class__, cls).__new__(cls, *args, **kwargs)
            setattr(cls, 'ins', insObject)
        return getattr(cls, 'ins')

class Singleton(ParentClass):
    pass



if __name__ == "__main__":
    ins1 = Singleton()
    ins2 = Singleton()
    print(ins1)
    print(ins2)
