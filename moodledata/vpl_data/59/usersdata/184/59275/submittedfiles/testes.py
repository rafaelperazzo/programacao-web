n=int(input('digite um número de 4 algarismos:'))
a=int(input('digite o primeiro algarismo do seu número:'))
b=int(input('digite o segundo algarismo do seu número:'))
c=int(input('digite o terceiro algarismo do seu número:'))
d=int(input('digite o quarto algarismo do seu número:'))
n1=str(a)+str(b)
n2=str(a)+str(c)
n3=str(a)+str(d)
n4=str(b)+str(a)
n5=str(b)+str(c)
n6=str(b)+str(d)
n7=str(c)+str(a)
n8=str(c)+str(b)
n9=str(c)+str(d)
n10=str(d)+str(a)
n11=str(d)+str(b)
n12=str(c)+str(d)
x1=n1*n9
x2=n2*n6
x3=n3*n5
x4=n1*n12
x5=n2*n11
x6=n3*n8
x7=n4*n9
x8=n4*n12
x9=n5*n10
x10=n6*n7
x11=n7*n11
x12=n8*n10
if x1==n or x2==n or x3==n or x4==n or x5==n or x6==n or x7==n or x8==n or x9==n or x10==n or x11==n or x12=n:
    print('é um vampiro')
else:
    print('não é um número vampiro')