# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite o valor do número de termos:'))
nu=2
de=1
cont=0
produto=1
while cont<n:
    produto=produto*(nu/de)
    if nu<de:
        nu=nu+2
    else:
        de=de+2
    cont=cont+1
resultado=produto*2
print('pi=%.5f' %resultado)
        
    
    
    