a=int(input('digite a:'))
b=int(input('digite b:'))
cont=0
x=a
y=b
while x%y!=0:
    r=x%y
    y=x
    x=y
    cont=cont+1
print(x)
print(cont)

