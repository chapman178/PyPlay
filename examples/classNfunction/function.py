def my_function(a, b = 10, *args, **kwargs):
    VAL[0] = 10
    print('a : ',a)
    print('b : ',b)
    if args:
        print('args : ',args)
    if kwargs:
        print('kwargs : ',kwargs)
    return

VAL = [1, 2, 3]
x = 1
y = 2
print('call 1 ------------')
my_function(x,y)
print('call 2 ------------')
my_function(x)
print('call 3 --------------')
my_function(b = y, a = x)
print('call 4 --------------')
my_function(x, y, 1, 2, 3 ,name = 1, end = 2)

print(VAL)
