'''
@author = xiaolin.wang
@description:
    通过@classmethod 实现单例模式
    同时可以实现懒加载模式
'''

class Singleton:

    @classmethod
    def getSingletonInstanceObjec(cls, *args, **kwargs):
        if not hasattr(cls, 'ins'):
            insObject = cls(*args, **kwargs)
            setattr(cls, 'ins', insObject)
        return getattr(cls, 'ins')

if __name__ == "__main__":
    ins1 = Singleton.getSingletonInstanceObjec()
    ins2 = Singleton.getSingletonInstanceObjec()
    print(ins1)
    print(ins2)
