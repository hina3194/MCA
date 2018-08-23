#####......TUPLES....#####
a=('hina','3rd Jan',"Name","DOB")
print(a)
##print(a[0]='umang') 
print(a[1])
print(len(a))
print('hina' in a)

t=12345, 54321, 'hello'
print(t)
print(type(t))

x,y,z=t
print(x)
print(y)
print(z)

##....using XOR
x=10
y=9
x=x^y
y=x^y
x=x^y
print(x)


#OR

x=10
y=9
x,y=y,x
print(x,y)
