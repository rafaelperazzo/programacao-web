import math
n=int(input('digite n: '))
termo=n
cont=0
valor=0
while termo!=0:
    termo=termo//10
    cont=cont+1
for i in range(1,cont+1,1):
    digito=n%10**(i)
    valor=valor+digito
print(valor)