
def my_decorator( func ):
    def onCall( *args, **kwargs):
        print("myDecorator: before {}".format(func.__name__))
        rc = func( *args, **kwargs)
        print("myDecorator: after {}".format(func.__name__))
        return rc
    return onCall



class myDecorator( object ):
    def __init__(self,  f ):
        self.f = f
    def __call__(self):
        print("myDecorator: before myFunction()")
        self.f(self)
        print("myDecorator: after myFunction()")

@my_decorator
def my_function():
    print("inside my_function()")


class MyClass():
    def __init__(self, a):
        print('running the  constructor')
        self.a = a

    def __str__(self):
        return'my str has this message,  Hello'

    # @staticmethod
    @my_decorator
    def my_method(self):
        print('inside mymethod')
        return

x = 1
B = MyClass(x)
B.my_method()
my_function()
