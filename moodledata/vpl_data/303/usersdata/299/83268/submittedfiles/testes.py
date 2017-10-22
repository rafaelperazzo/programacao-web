x=int(input(''))
while x<0:
    x=int(input(''))
while x>0:
    y=x
    x=x-1
    y=y*(y-1)
print(y)