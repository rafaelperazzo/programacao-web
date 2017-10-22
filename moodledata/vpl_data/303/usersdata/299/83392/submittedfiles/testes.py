x=int(input(''))
cont=0
while x<0:
    x=int(input(''))
while x>0:
    y=x
    x=x-1
    cont=x*y
print(cont)