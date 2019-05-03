

class MyClass():
    CLASS_VAR = 5.0

    def __init__(self, a, b):
        print('running the  constructor')
        self.a = a
        self.b = b
        self.c = self.CLASS_VAR
        print('global VAR : ',VAR)

    def __str__(self):
        return'my str has this message,  Hello'

    def my_method(self,c,d):
        print()
        VAR = 10
        print('method local VAR : ',VAR)
        print('CLASS_VAR : ',self.CLASS_VAR)
        print(f'my variables {c} and {d}')
        return 'fantastic'

VAR = 7
CLASS_VAR = 'a' # ignores value
A = MyClass(1,2)
print(A)
print('a : ',A.a)
print('b : ',A.b)
print('c : ',A.c)
print(A.my_method('hello','bro'))
print('final var : ',VAR)
