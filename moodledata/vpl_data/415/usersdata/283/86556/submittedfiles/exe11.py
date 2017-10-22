# -*- coding: utf-8 -*-


a=int(input('Digite o número: '))
while (a>99999999 or a<10000000):
    print('Número Inválido!')
    print('Tente um número de oito algarismos.')
    a=int(input('Digite o número: '))
    break
b=a//10000000
d=a-b*10000000
e=d//1000000
f=d-e*1000000
g=f//100000
h=f-g*100000
i=h//10000
j=h-i*10000
k=j//1000
l=j-k*1000
m=l//100
n=l-m*100
o=n//10
p=n-o*10

R= b + e + g + i + k + m + o + p

print(R)
    
    
      
     