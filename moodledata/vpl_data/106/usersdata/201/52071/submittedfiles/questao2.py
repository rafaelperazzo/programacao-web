# -*- coding: utf-8 -*-
x1=int(input('Digite a primeira dezena sorteada:'))
x2=int(input('Digite a segunda dezena sorteada:'))
x3=int(input('Digite a terceira dezena sorteada:'))
x4=int(input('Digite a quarta dezena sorteada:'))
x5=int(input('Digite a quinta dezena sorteada:'))
x6=int(input('Digite a sexta dezena sorteada:'))
y1=int(input('Digite o primeiro número da aposta:'))
y2=int(input('Digite o segundo número da aposta:'))
y3=int(input('Digite o terceiro número da aposta:'))
y4=int(input('Digite o quarto número da aposta:'))
y5=int(input('Digite o quinto número da aposta:'))
y6=int(input('Digite o sexto número da aposta:'))
cont=0
if x1==y1 or x1==y2 or x1==y3 or x1==y4 or x1==y5 or x1==y6:
    cont=cont+1
if x2==y1 or x2==y2 or x2==y3 or x2==y4 or x2==y5 or x2==y6:
    cont=cont+1
if x3==y1 or x3==y2 or x3==y3 or x3==y4 or x3==y5 or x3==y6:
    cont=cont+1
if x4==y1 or x4==y2 or x4==y3 or x4==y4 or x4==y5 or x4==y6:
    cont=cont+1
if x5==y1 or x5==y2 or x5==y3 or x5==y4 or x5==y5 or x5==y6:
    cont=cont+1
if x6==y1 or x6==y2 or x6==y3 or x6==y4 or x6==y5 or x6==y6:
    cont=cont+1
if cont==3:
    print('terno')
elif cont==4:
    print('quadra')
elif cont==5:
    print('quina')
elif cont==6:
    print('sena')
elif cont<3:
    print('azar')