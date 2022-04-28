'''
@author = xiaolin.wang
@description:
    元类实现
'''

class MetaClass(type):
    def __call__(self, *args, **kwargs):
        if not hasattr(self, 'ins'):
            insObject = super(__class__, self).__call__(*args, **kwargs)
            setattr(self, 'ins', insObject)
        return getattr(self, 'ins')

class Singleton(object, metaclass=MetaClass):
    pass


if __name__ == "__main__":
    ins1 = Singleton()
    ins2 = Singleton()
    print(ins1)
    print(ins2)
