class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError('ba chem jnjel sahmani nor')
        self.fdel(instance)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError('Sahmai nor ogtagorci')
        return self.fget(instance)

    def __set__(self, instance, value):
        if self is None:
            raise AttributeError('sahmani nor ogtagorci')
        self.fset(instance, value)

    def deleter(self, fdel):
        """Pordzum em jnjel """
        return type(self)(self.fget, self.fset, fdel, self.__doc__)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)


class Jan:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @MyProperty
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        print(f'{self.__x} er')
        self.__x = value
        print(f'darav {self.__x}')

    @x.deleter
    def x(self):
        print('Deleting x,,, jnjvec')
        del self.__x

obj = Jan(12,1)
print(obj.x)
obj.x = 16
print(obj.x)
del obj.x
