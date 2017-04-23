# -*- coding: utf-8 -*-
peso=float(input('digite peso:'))
altura=float(input('digite altura:'))
IMC=peso/(altura*altura)
if IMC<20:
    print('ABAIXO')
elif 20<=IMC<=25:
    print('NORMAL')
else:
    if 25<IMC<=30:
        print('SOBREPESO')
    elif 30<IMC<=40:
        print('OBESIDADE')
    else:
        if IMC>40:
            print('OBESIDADE GRAVE')