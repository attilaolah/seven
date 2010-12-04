def decorate(cls):
    cls.__repr__ = lambda self: '<decorated object at %s>' % id(self)
    return cls


@decorate
class Foo(object):
    """Example decorated class."""


print 'Foo:', Foo()
