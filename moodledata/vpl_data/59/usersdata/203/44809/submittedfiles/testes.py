import math
n=int(input('digite n: '))
termo=n
cont=0
valor=0
while termo!=0:
    termo=termo//10
    cont=cont+1
valor=n%10
print(valor)