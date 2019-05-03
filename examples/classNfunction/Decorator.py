
class myDecorator( object ):
    def __init__(self,  f ):
        self.f = f
    def __call__(self):
        print("myDecorator: before myFunction()")
        self.f()
        print("myDecorator: after myFunction()")

@myDecorator
def my_function():
    print("inside my_function()")


class MyClass():
    def __init__(self, a):
        print('running the  constructor')
        self.a = a

    def __str__(self):
        return'my str has this message,  Hello'

    @staticmethod
    @myDecorator
    def my_method():
        print('inside mymethod')
        return

x = 1
B = MyClass(x)
B.my_method()
my_function()
