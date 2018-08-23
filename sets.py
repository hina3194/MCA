s={1,2,3}
print(s)
print(type(s))
Name={'firstname','lastname'}
print(Name)
print(type(Name))
s={3,1,5,8,2}
print(s)
print(type(s))
empty_set=set()
set_from_list=set([1,2,1,4,3])
print(set_from_list)
basket={"apple","orange","apple","pear","banana"}
print(basket)
print("mango" in basket)
 ##function in sets...##
a=set("missipp1")
print(a)
a.add('r')
print(a)
a.remove('m')
print(a)
a.pop()
print(a)
a.discard('x')
print(a)
a.clear()

## two sets  ##

y=set("abcdefg")
z=set("adefg")
print(y-z) #set diff.
y=set("abcdefg")
z=set("adefg")
print(y|z) #union
y=set("abcdefg")
z=set("adefg")
print(y&z)
y=set("abcdefg")
z=set("adefg")
print(y^z)





