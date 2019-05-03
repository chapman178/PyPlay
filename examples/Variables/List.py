x = [1,2,3,1]
print(type(x))
print(dir(x))
print('count:',x.count(1)) # 2, number of times the input occurs
print('index:',x.index(1)) # returns location of input (first occurance)
print(x,' : x')
try:
    x[0] = 1.2 # lists are mutable
except(TypeError) as e:
    print(e)
print(x,' : x[0]= 1.2')
x.append(7)
print(x,' : x.append(7) - on end')
x.extend([2,3])
print(x,' : x.extend([2,3]) - on end')
x.insert(3,10)
print(x,' : x.insert(3,10) - add 10 in space 3')
x.pop()
print(x,' : x.pop() - remove last item')
x.remove(2)
print(x,' : x.remove(2)- first occurance')
x.sort()
print(x,' : x.sort()')
x.reverse()
print(x,' : x.reverse()')
x.clear()
print(x,' : x.clear:')