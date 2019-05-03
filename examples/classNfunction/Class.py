

class MyClass():
    CLASS_VAR = 5.0

    def __init__(self, a, b):
        print('running the  constructor')
        self.a = a
        self.b = b
        self.c = self.CLASS_VAR

    def __str__(self):
        return'my str'

    def my_method(self,c,d):
        print(f'my variables {c} and {d}')
        return 'fantastic'


A = MyClass(1,2)
print(A)
print(A.a)
print(A.b)
print(A.c)
print(A.my_method('hello','bro'))

