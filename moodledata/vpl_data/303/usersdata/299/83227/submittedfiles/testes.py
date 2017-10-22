x=int(input(''))
while x<0:
    x=int(input(''))
while x>0:
    y=x
    y=y*(y-1)
    x=x-1
print(x)