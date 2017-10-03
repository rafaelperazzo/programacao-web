# -*- coding: utf-8 -*-
peso= float(input('digite seu peso em quilogramas: '))
altura= float(input('digite sua altura em metros: '))
imc=((peso)/((altura)^2))
if imc<20 :
    print('imc<20 - ABAIXO')
elif 20<=imc<=25 :
    print('20<=imc<=25 - NORMAL')
elif 25<imc<=30 :
    print('25<imc<=30 - SOBREPESO')
elif 30<imc<=40 :
    print('30<imc<=40 - OBESIDADE')
else :
    print('imc>40 - OBESIDADE GRAVE')
