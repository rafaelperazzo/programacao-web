# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

// A seguinte função recebe um valor 'x' tira o valor do módulo,
// ou seja, mostra ele positivo.
def valorabsoluto(x):
    if (x<0):
        x=x*(-1)
    else:
        x=x*1
    return(x)
    
def pi(m):
    cont=0
    soma=3
    a=0
    b=2
    for i in range (1, m+1, 1):
        a=4/(b*(b+1)*(b+2))
        cont=cont+1
        if (cont%2==1):
            soma=soma+a
        if (cont%2==0):
            soma=soma-a    
        b=b+2
    return(soma)
#A função 'pi(m)' mostra o valor de PI. O usuário pode colocar qualquer entrada 
#que o resultado sempre será um valor próximo de 3,14159...    

def fat(d):
    f=1
    while (d>0):
        f=f*d
        d=d-1
    return(f)
#'fat(d)' é a função do fatorial. Ela resolve o fatorial de qualquer número, 
#mas nesse caso será preciso fazer o fatorial só do denominador do cosseno.  
    
def cos(x, epsilon):
    cont=0
    soma=1
    d=2
    c=(x**d)/fat(d)
    while (c>epsilon):    
        cont=cont+1
        if (cont%2==1):
            soma=soma-c
        if (cont%2==0):
            soma=soma+c
        d=d+2
        c=(x**d)/fat(d)    
    return(soma)
#A função 'cos(x, epsilon)' resolve o cosseno. Nessa função foi utilizado como
#critério de parada 'while(c>epsilon)' pois só será necessário calcular o 
#cosseno enquanto o próprio for maior do que o valor do epsilon.
    
def razaoaurea(m, epsilon):
    x=pi(m)/5
    g=cos((x),(epsilon))
    razao=2*g
    return(razao)
#A função 'razaoaurea(m, epsilon)' é onde se calcula a Razão Áurea.
#Foram utilizadas as funções acima para resolver a Razão Áurea.


m=int(input('Digite o número de termos para PI: '))
#O valor de 'm' deve ser de 1 a 2000.
epsilon=float(input('Digite o epsilon para o cálculo da razão aurea: '))
#O valor de 'epsilon' deve ser entre 0 e 1.
print('%.15f' %pi(m))
print('%.15f' %razaoaurea(m, epsilon))