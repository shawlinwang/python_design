'''
@author = xiaolin.wang
@description:
    使用装饰器实现单例模式
'''
def warpper(clsObject):
    def inner(*args, **kwargs):
        if not hasattr(clsObject, 'ins'):
            insObject = clsObject(*args, **kwargs)
            setattr(clsObject, 'ins', insObject)
        return getattr(clsObject, 'ins')
    return inner

@warpper
class Singleton:
    pass

if __name__ == "__main__":
    ins1 = Singleton()
    ins2 = Singleton()
    print(ins1)
    print(ins2)

