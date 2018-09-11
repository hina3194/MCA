def multiple_return (x):
    return x*1,x*2,x*3

A,B,C = multiple_return(3)
print(A)
print(B)
print(C)

## Function square ###
def square():
     new_value=4**2
     print(new_value)
square()

## Functio CUBE
def cube():
    new_value=4*4*4
    print(new_value)
cube()

#function with argument
def cube (x):
    return x*x*x
a=cube(3)
print(a)


## docstrings

def cube(value):
    """Return the cube of value"""
    new_value=value*value*value
    return new_value
    print(new_value)
# docstring
def multiple_value(a,b):
    """Return multiple of two value"""
    multi=a*b
    print(multi)
    return multi
   

result,r = multi(3,5)


    

            
