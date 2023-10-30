d1={1:"hello",2:"hi",'a':'welcome'}
print(d1.keys())
print(d1.values())
print(d1.items())
print(d1.get('a'))

#copy of dict
newd=d1.copy()
print("\ncopy dict -\n",newd)

#remove specific element
print(d1.pop(1))
print("\nremove 1\n",d1)

#remove last element
print(d1.popitem())
print("\nafter remove last element",d1)

#update 
d2={4:"welcome"}
d1.update(d2)
print("\nupdate dict - \n",d1)

d1.clear()
print("\nafter clear",d1)

d3={'a','b','c'}
d4=dict.fromkeys(d3,1)
print(d4)
