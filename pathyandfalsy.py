##...Falsy...##
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(''))

##...Empty data structure are 'Falsy'...##
data=[]
if data:
    print("process(data)")
else:
    print("there is no data")
      
