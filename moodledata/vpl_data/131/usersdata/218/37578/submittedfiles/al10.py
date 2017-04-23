# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite o valor de n:'))
numerador=2
denominador=1
termo=numerador/denominador
i=1
while i<=n+1:
    if denominador<numerador:
        denominador=denominador+2
    else:
        numerador=numerador+2
termo=termo*(numerador/denominador)
print('%.5.f'%termo)