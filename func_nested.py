## Nested Function ##

def multi(x1,x2,x3):
    
    def inner(x):
        return x % 2 + 5
    return(inner(x1),inner(x2),inner(x3))
print(multi(1,2,3))

####...Using nonlocal....###


        
        
       
        
