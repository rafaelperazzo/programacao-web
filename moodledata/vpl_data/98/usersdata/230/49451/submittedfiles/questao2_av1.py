# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
A1=int(input('Digite primeira aposta: '))
A2=int(input('Digite segunda aposta: '))
A3=int(input('Digite terceira aposta: '))
A4=int(input('Digite quarta aposta: '))
A5=int(input('Digite quinta aposta: '))
A6=int(input('Digite sexta aposta: '))
S1=int(input('Digite primeiro número sorteado: '))
S2=int(input('Digite segundo número sorteado: '))
S3=int(input('Digite terceiro número sorteado: '))
S4=int(input('Digite quarto número sorteado: '))
S5=int(input('Digite quinto número sorteado: '))
S6=int(input('Digite sexto número sorteado: '))
if A1==S1 and A2==S2 and A3==S3 or A4==S4 and A5==S5 and A6==S6:
    print('Terno')
if A1==S2 and A2==S3 and A3==S4 or A4==S1 and A5==S2 and A6==S3:
    print('Terno')
if A1==S3 and A2==S4 and A3==S5 or A4==S2 and A5==S2 and A6==S3:
    print('Terno')
if A1!=S1 and A2!=S2 and A3!=S3 and A4!=S4 and A5!=S5 and A6!=S6:
    print('Azar')