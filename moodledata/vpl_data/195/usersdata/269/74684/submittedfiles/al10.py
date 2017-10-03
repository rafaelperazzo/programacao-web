# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('n: '))

i=2
a=3
contador=1
numerador=1
b=1
denominador=1

if n%2==0:
    while contador<=n/2:
        numerador=(i*i)*numerador
        i=i+2
        denominador=denominador*(a*b)
        a=a+2
        b=b+2
        contador=contador+1
    pi=(numerador/denominador)*2
    print(pi)

if n%2==1:
    n=n-1
    while contador<=n/2:
        numerador=(i*i)*numerador
        i=i+2
        denominador=denominador*(a*b)
        a=a+2
        b=b+2
        contador=contador+1
    numerador=numerador*(i+2) 
    denominador=denominador*a

    pi=(numerador/denominador)*2
    print(pi)
    

        