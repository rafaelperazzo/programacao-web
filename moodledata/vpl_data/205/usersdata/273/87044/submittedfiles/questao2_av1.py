# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a=int(input('Digite o numero escolhido: '))
b=int(input('Digite o numero escolhido: '))
c=int(input('Digite o numero escolhido: '))
d=int(input('Digite o numero escolhido: '))
e=int(input('Digite o numero escolhido: '))
f=int(input('Digite o numero escolhido: '))

asort=int(input('Digite o numero sorteado: '))
bsort=int(input('Digite o numero sorteado: '))
csort=int(input('Digite o numero sorteado: '))
dsort=int(input('Digite o numero sorteado: '))
esort=int(input('Digite o numero sorteado: '))
fsort=int(input('Digite o numero sorteado: '))
a1=a
cont=0
while true a1!=a:
    if a==asort or a==bsort or a==csort or a==dsort or a==esort or a==fsort:
        cont=cont+1
        a=b
        b=c
        c=d
        d=e
        e=f
        
if cont==3:
    print('Terno')
elif cont==4:
    print('Quadra')
elif cont==5:
    print('Quina')
elif cont==6:
    print('Sena')
else:
    print('Azar')
            
