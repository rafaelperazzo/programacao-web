# -*- coding: utf-8 -*-
P1=int(input('digite um valor para o peso da esquerda'))
C1=float(input('digite um valor para o cumprimento esquerdo da gangorra'))
P2=int(input('digite um valor para o peso da direita'))
C2=float(input('digite um valor para o comprimento direito da gangorra'))
if C1*P1==C2*P2:
    print(''0'')
elif C1*P1>C2*P2:
    print('-1')
else:
    print('1')
    

