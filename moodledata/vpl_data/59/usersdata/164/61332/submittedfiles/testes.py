# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

'''
A seguinte função recebe um valor x
e retorna o módulo desse, ou seja,
mostra ele positivo.
'''
def valorabsoluto(x):
    if (x<0):
        x=x*(-1)
    else:
        x=x*1
    return(x)
    
'''
A função a seguir mostra o valor de PI. 
O usuário digita o número de termos para
calcular PI, e o resultado sempre será
algo próximo de 3,14159...
'''
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

'''
A função 'fat(d)' calcula o fatorial.
Nesse caso, será preciso calcular 
somente o denominador do cosseno.
'''
def fat(d):
    f=1
    while (d>0):
        f=f*d
        d=d-1
    return(f)

'''
A função abaixo resolve o cosseno. 
Nela foi utilizado como critério 
de parada 'while(c>epsilon)'
pois só será necessário calcular o
cosseno enquanto o próprio for 
maior do que o valor do epsilon.
'''    
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

'''
A função 'razaoaurea(m, epsilon)' 
é onde se calcula a Razão Áurea.
Foram utilizadas as funções 
acima para resolver a Razão Áurea.
'''     
def razaoaurea(m, epsilon):
    x=pi(m)/5
    g=cos((x),(epsilon))
    razao=2*g
    return(razao)


m=int(input('Digite o número de termos para PI: '))
#O valor de 'm' deve ser de 1 a 2000.
epsilon=float(input('Digite o epsilon para o cálculo da razão aurea: '))
#O valor de 'epsilon' deve ser entre 0 e 1.
print('%.15f' %pi(m))
print('%.15f' %razaoaurea(m, epsilon))