## returning function##

def raise_val(n):
    """return the inner function """
    def inner(x):
        raised=x**n
        return raised
    return inner
a=raise_val(2)
b=raise_val(3)
print(a(2),b(3))
