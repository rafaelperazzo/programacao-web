# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a = int(input('Digite o primeiro numero entre 1 e 99: '))
b = int(input('Digite o segundo numero entre 1 e 99 diferente do anterior: '))
c = int(input('Digite o terceiro numero entre 1 e 99 diferente dos anteriores: '))
d = int(input('Digite o quarto numero entre 1 e 99 diferente dos anteriores: '))
e = int(input('Digite o quinto numero entre 1 e 99 diferente dos anteriores: '))
f = int(input('Digite o sexto numero entre 1 e 99 difernte dos anteriores: '))
n1 = int(input('Digite o primeiro numero entre 1 e 99: '))
n2 = int(input('Digite o segundo numero entre 1 e 99 diferente do anterior: '))
n3 = int(input('Digite o terceiro numero entre 1 e 99 diferente dos anteriores: '))
n4 = int(input('Digite o quarto numero entre 1 e 99 diferente dos anteriores: '))
n5 = int(input('Digite o quinto numero entre 1 e 99 diferente dos anteriores: '))
n6 = int(input('Digite o sexto numero entre 1 e 99 diferente dos anteriores: '))
acerto = 0
if a//n1 == 1 or a//n2 == 1 or a//n3 == 1 or a//n4 == 1 or a//n5 == 1 or a// n6== 1:
    acerto1 = acerto + 1
elif b//n1 == 1 or b//n2 == 1 or b//n3 == 1 or b//n4 == 1 or b//n5 == 1 or b// n6== 1:
    acerto2 = acerto + 1
elif c//n1 == 1 or c//n2 == 1 or c//n3 == 1 or c//n4 == 1 or c//n5 == 1 or c// n6== 1:
    acerto3 = acerto + 1
elif d//n1 == 1 or d//n2 == 1 or d//n3 == 1 or d//n4 == 1 or d//n5 == 1 or d// n6== 1:
    acerto4 = acerto + 1
elif e//n1 == 1 or e//n2 == 1 or e//n3 == 1 or e//n4 == 1 or e//n5 == 1 or e// n6== 1:
    acerto5 = acerto + 1
elif f//n1 == 1 or f//n2 == 1 or f//n3 == 1 or f//n4 == 1 or f//n5 == 1 or f// n6== 1:
    acerto6 = acerto + 1
    acertofinal = acerto1 + acerto2 + acerto3 + acerto4 + acerto5 + acerto6
        if acertofinal<3:
            print('azar')
        elif acertofinal==3:
            print('terno')
        elif acertofinal==4:
            print('quadra')
        elif acertofinal==5:
            print('quina')
        elif acertofinal==6:
            print('sena')




