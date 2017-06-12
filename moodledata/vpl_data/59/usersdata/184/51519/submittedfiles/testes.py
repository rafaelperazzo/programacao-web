import math
n=int(input('digite a quantidade de números a serem mostrados:'))
a=int(input('digite a:'))
b=int(input('digite b:'))
cont=0
i=1
while n>cont:
    if i%a==0 and i%b==0:
        print(i)
        cont=cont+1
    i=i+1
