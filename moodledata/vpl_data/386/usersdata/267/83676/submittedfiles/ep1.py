# -*- coding: utf-8 -*-
#FUNÇÃO
def raiz_quadrada(x,epsilon):
    r0=x
    while (r1-r0)<epsilon:
        r1=(1/2)*(r0+(x/r0))
        r0=r1
    



#PROGRAMA PRINCIPAL
e=0
while e<=0:
    e=int(input('Precisão para cálculo: '))
n=int(input('Número de equações: '))
cont=0
print('               Raízes de Equações Quaadráticas')
print('-------------------------------------------------------------------')
print('     coeficientes          tipo das')
print('  a       b        c       soluções        raiz 1           raiz 2')
print('--------------------------------------------------------------------)
while cont<=n:
    a=float(input('Informe o valor do coeficiente a: '))
    b=float(input('Informe o valor do coeficiente b: '))
    c=float(input('Informe o valor do coeficiente c: '))
    delta=(b*b)-(4*a*c)
    if delta>0:
        x1=(-b+raiz_quadrada(delta,e))/(2*a)
        x2=(-b-raiz_quadrada(delta,e))/(2*a)
        
    elif delta<0:
        #fazer
    else:
        
    
