x = {'W':[1,2,3],'S':[4,5,6]}
print(type(x))
print(dir(x))
keys = ('W', 'S')
val = [1]
print(x.fromkeys(keys,val),'x.fromkeys(keys,val) - create dictionary with name keys , each has value val')
print(x,' : base dictionary')
x['D'] = [6, 7, 8,9]
print(x,' : x["D"]= [6,7,8,9] - add another dict item')
x.update({'D':[5, 8]})
print(x,' : update({"D":[5,8]}) - update with another dictionary')
print(x.get('D'), ' : get D')
print(x.items(), ' : items ')
print(x.keys(), ' : keys ')
print(x.pop('W'), ' : pop("W") output')
print(x, ' : x after pop')
print(x.setdefault('S','ignore'), ' : setdefault key and value.  sets value only if key does not exist')