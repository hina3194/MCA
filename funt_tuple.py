#def raise_both(value1,value2):
    #"""Raise value1 to the power of value2"""
   # new_value1=value1**value2
   # new_value2=value2**value1
    #new_tuple=(new_value1,new_value2)
    #return new_tuple

###global vs. local scope

new_value=10
def square(value):
    
    #"""Returns the square of the number"""
    new_value2=new_value**2
    print(new_value2)
square(3)
new_value=20
square(3)

##
new_value=10
def square(value):
    
    #"""Returns the square of the number"""
    global new_value
    new_value2=new_value**2
    return new_
square(3)
new_value=20
square(3)


    
