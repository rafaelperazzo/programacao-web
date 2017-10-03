# -*- coding: utf-8 -*-

#lendo preço de etiqueta
etiqueta = float(input('Preço de etiqueta do produto: '))

#lendo tipo de pagamento
codigo = int(input('Codigo de pagamento: '))

if (codigo==1):
    total = etiqueta*0.85
    print('%.2f' % total)
elif (codigo==2):
    total = etiqueta*0.90
    print('%.2f' % total)
elif (codigo==3):
    print('%.2f' % etiqueta)
elif (codigo==4):
    total = etiqueta*1.15
    print('%.2f' % total)


