# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade:'))
b=[]
somaimpares=0
somapares=0
contimpares=0
contpares=0

for i in range(0,n,1):
    b=float(input('Digite um valor:'))
    b.append(b)

for i in range(0,len(v),1):
    if b[i]%2==1:
        somaimpares=somaimpares+b[i]
        contimpares=contimpares+1
    if b[i]%2==0:
        somapares=somapares+b[i]
        somapares=somapares+1
print('%.2f'%somaimpares)
print('%.2f'%somapares)
print('%.2f'%contimpares)
print('%.2f'%contpares)
print(b)
       
        
    