# -*- coding: utf-8 -*-
P1 = float(input('Digite o peso da crianca do lado esquerdo: '))
C1 = float(input('Digite o comprimento do lado da crianca do lado esquerdo: '))
P2 = float(input('Digite o peso da crianca do lado direito: '))
C2 = float(input('Digite o comprimento do lado da crianca do direito: '))
if P1*C1==P2*C2:
    print(str("'0'"))
elif P1*C1>P2*C2:
    print(str("'-1'"))
elif P1*C1<P2*C2:
    print(str("'1'")
    