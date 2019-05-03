class Transaction(object):
def __init__(self, val1, val2):
    self.val1 = val1
    self.val2 = val2
def __sub__(self, other):
    return self.val1 - other.val1
def __str__(self):
    return "val1={},val2={}".format(self.val1, self.val2)
buy = Transaction(10.00, 23)
sell = Transaction(7.00,24)
result = buy - sell
print(buy)
print(sell)
print(result, type(result))