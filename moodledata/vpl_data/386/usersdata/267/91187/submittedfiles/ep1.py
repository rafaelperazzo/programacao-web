# -*- coding: utf-8 -*-

#FUNÇÃO
def raiz_quadrada(x,epsilon):
    r_atual=x
    r_prox=(1/2)*(r_atual+(x/r_atual))
    while abs((r_prox-r_atual))>epsilon:
        r_atual=r_prox
        r_prox=(1/2)*(r_atual+(x/r_atual))
    return (r_prox)
    

#PROGRAMA PRINCIPAL
e=0
while e<=0:
    e=float(input('Precisão para cálculo: '))
n=int(input('Número de equações: '))
cont=0
print('               Raízes de Equações Quadráticas')

while cont<n:
    cont=cont+1
    a=float(input('Informe o valor do coeficiente a: '))
    b=float(input('Informe o valor do coeficiente b: '))
    c=float(input('Informe o valor do coeficiente c: '))
    
    print('--------------------------------------------------------------------')
    print('     coeficientes           tipo das')
    print('  a       b        c        soluções           raiz 1        raiz 2')
    print('--------------------------------------------------------------------')
    
    delta=(b*b)-(4*a*c)
    if a==0:
        print('%.4f  %.4f  *** ERRO: equação não é do segundo grau' %(a,b,c))
    else:
        if delta>0:
            x1=(-b+raiz_quadrada(delta,e))/(2*a)
            x2=(-b-raiz_quadrada(delta,e))/(2*a)
            print('%.4f  %.4f  %.4f  reais simples       %.4f          %.4f' %(a,b,c,x1,x2))
        
        elif delta<0:
            delta=-delta
            x1=-b/(2*a)
            x2=x1
            raiz_delta=(raiz_quadrada(delta,e))/(2*a)
            print('%.4f  %.4f  %.4f    complexas     %.4f + i*%.4f      %.4f - i*%.4f' %(a,b,c,x1,raiz_delta,x2,raiz_delta))
        else:
            x1=-b/(2*a)
            x2=x1
            print('%.4f  %.4f  %.4f    real dupla    %.4f     %.4f' %(a,b,c,x1,x2))
            
            
        
