
x = (1,2,3,1)
print(type(x))
print(dir(x))
try:
    x[0] = 1.2 # tuples are immutable
except(TypeError) as e:
    print(e)

print(x.count(1)) # 2, number of times the input occurs
print(x.index(1)) # returns location of input (first occurance