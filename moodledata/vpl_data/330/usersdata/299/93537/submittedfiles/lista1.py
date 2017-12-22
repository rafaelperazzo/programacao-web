# -*- coding: utf-8 -*-
n_valores=int(input('Digite quantos valores sua lista terá: '))
l=[]
contpar=0
contimpar=0
somapar=0
somaimpar=0
for i in range(0,n_valores,1):
    l.append(int(input('Digite o valor %d: ' %(i+1))))

for i in range(0,n_valores,1):
    if l[i]%2==0:
        contpar+=1
        somapar+=l[i]
    else:
        contimpar+=1
        somaimpar+=l[i]
print(somaimpar)
print(somapar)
print(contimpar)
print(contpar)
print(l)


    

