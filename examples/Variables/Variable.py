
# int
x = 12
print(type(x)) # int
print(dir(x))
print(x.bit_length()) # 4

# float
x = 1.5
print(type(x)) # float
print(dir(x))
print(x.as_integer_ratio()) # (3,2)
print(x.is_integer()) # False
x=1.0
print(x.is_integer()) # True

# complex
x = 1 + 2j
print(type(x)) # complex
print(dir(x))
print(x.real) # 1.0
print(x.imag) # 2.0
print(x.conjugate()) # 1 - 2j
print(x+x) #2 + 4j
print(x*x) # -3 + 4j