# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite o vaçlor de n:'))
i=0
numerador=2
denominador=1
produto=1
while i<=n:
   produto=produto*numerador/denominador
   if i%2==1:
       numerador=numerador+2
   else:
       denominador=denominador+2
    i=i+1
pi=produto*2
print(pi)