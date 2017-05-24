a=int(input('digite a:'))
b=int(input('digite b:'))
cont=1
x=a
y=b
while x%y!=0:
    r=x%y
    x=y
    y=r
    cont=cont+1
print(y)
print(cont)

