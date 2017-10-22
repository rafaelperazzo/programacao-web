# -*- coding: utf-8 -*-

#FUNÇÃO
def raiz_quadrada(x,epsilon):
    r_atual=x
    r_prox=(1/2)*(r_atual+(x/r_atual))
    while abs((r_prox-r_atual))>epsilon:
        r_atual=r_prox
        r_prox=(1/2)*(r_atual+(x/r_atual))
        print(r_prox)
        print(r_atual)
    return (r_prox)
    


#PROGRAMA PRINCIPAL
e=0
while e<=0:
    e=int(input('Precisão para cálculo: '))
n=int(input('Número de equações: '))
cont=0
print('               Raízes de Equações Quadráticas')
print('-------------------------------------------------------------------')
print('     coeficientes          tipo das')
print('  a       b        c       soluções        raiz 1           raiz 2')
print('-------------------------------------------------------------------')
while cont<=n:
    cont=cont+1
    a=float(input('Informe o valor do coeficiente a: '))
    b=float(input('Informe o valor do coeficiente b: '))
    c=float(input('Informe o valor do coeficiente c: '))
    delta=(b*b)-(4*a*c)
    if delta>0:
        x1=(-b+raiz_quadrada(delta,e))/(2*a)
        x2=(-b-raiz_quadrada(delta,e))/(2*a)
        print('%.3f %.3f %.3f     reais simples         %.3f    %.3f' %(a,b,c,x1,x2))
        
    elif delta<0:
        #fazer
        print('NÃO')
    
        
    
