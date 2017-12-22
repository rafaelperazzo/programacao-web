# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def raiz2(x,epsilon):
    if x>=0:
        r(0)=x
        n=0
        while ((r(n)+1)-r(n))<=e:
            (r(n)+1)=(1/2)*(r(n) + (x/r(n)))
            n=n+1
        return(r((n)+1))
    else:
        r(0)=x
        n=0
        while ((r(n)+1)-r(n))<=e:
            (r(n)+1)=(1/2)*(r(n) + ((-x/r(n)))
            n=n+1
        return(r((n)+1))
        
def baskara(a,b,c):
    delta= (b**2) - 4*a*c
    if delta>=0:
        x1=((-b)+(raiz2(delta,epsilon)))/(2*a)
        x2=((-b)-(raiz2(delta,epsilon)))/(2*a)
    else:
        x1=((-b)+(i*(raiz2(delta,epsilon))))/(2*a)
        x2=((-b)-(i*(raiz2(delta,epsilon))))/(2*a)
    
    return(delta)    
    return(x1)
    return(x2)
        
        
epsilon=float(input('digite o espsilon: '))
nequacoes=int(input('digite o número de equações: '))

for equação in range(0,n,1):
    a=int(input('Digite o a da equação: '))
    b=int(input('Digite o b da equação: '))
    c=int(input('Digite o c da equação: '))
    
    if a!=0:
        baskara(a,b,c)
        if delta>0 and x1!=x2:
            print(a)  print(b)  print(c)  print('reais simples')  print(x1)  print(x2)
        elif delta=0:
            print(a)  print(b)  print(c)  print('real dupla')  print(x1)  print(x2)
        else:
            print(a)  print(b)  print(c)  print('complexas')  print(x1) print(x2)
    else: 
        print('*** ERRO: equação não é do segundo grau! ***')