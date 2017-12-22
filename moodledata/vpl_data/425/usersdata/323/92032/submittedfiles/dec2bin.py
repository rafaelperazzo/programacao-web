# -*- coding: utf-8 -*-
p=int(input('Digite o número menor: '))
q=int(input('Digite o número maior: '))

p1 = p
cont=0

while p>0:
    cont=cont+1
    p=p//10
i=0
while q>0:
    if q%(10**cont) ==p1:
        i=0
        break
    else:
        i=i+1
    q=q//10
    
if i!=0:
    print ('N')
elif i==0:
    print('S')
    