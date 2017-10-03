# -*- coding: utf-8 -*-
peso= float(input('Digite o peso: '))
altura= float(input('Digite altura: '))
IMC= peso/(altura)**2
if IMC<20:
    print('ABAIXO')
else:
    if 20<=IMC<=25:
        print('NORMAL')
    else:
        if 25<IMC<=30:
            print('SOBREPESO')
        else:
            if 30<IMC<=40:
                print('OBESIDADE')
            else:
                if IMC>40:
                     print('OBESIDADE GRAVE')