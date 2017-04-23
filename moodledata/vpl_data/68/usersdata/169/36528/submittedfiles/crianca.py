# -*- coding: utf-8 -*-
P1=float(input('Digite o Peso da Criança do Lado Esquerdo da Gangorra:'))
C1=float(input('Digite o Comprimento do Lado Esquerdo da Gangorra:'))
P2=float(input('Digte o Peso da Criança do Lado Direito da Gangorra:'))
C2=float(input('Digite o Comprimento do Lado Direito da Gangorra:'))
X=(P1*C1)
Y=(P2*C2)
if (X>Y):
    print('-1')
if (Y>X):
    print('1')
else:
    print('0')
