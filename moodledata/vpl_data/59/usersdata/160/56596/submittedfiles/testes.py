from __future__ import division 

def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
    else:
        x=x*1
    return(x)

def calcula_pi(m):
    soma=0
    denominador=2
    for i in range(1,m+1,1):
        if i%2==1:
            soma=soma+(4/((denominador)*(denominador+1)*(denominador+2)))
        else:
            soma=soma-(4/((denominador)*(denominador+1)*(denominador+2)))
        denominador=denominador+2
    pi=3+(soma)
    return(pi)
    
def fatorial(n):
    i=1
    fatorial=1
    while i<=n:
        fatorial=fatorial*i
        i=i+1
        
def calcula_co_seno(z,epsilon):
    expoente=2
    i=1
    termo=((z**expoente)/(fatorial(expoente)))
    soma=0
    while termo>epsilon:
        if i%2==1:
            soma=soma-termo
        else:
            soma=soma+termo
        i=i+1
        denominador=denominador+2
        termo=((z**expoente)/(fatorial(expoente)))
    cosseno=1+(soma)
    return(cosseno)
    
def calcula_razao_aurea(m,epsilon):
    formula=calcula_co_seno((calcula_pi(m))/(5/epsilon))
    razaoaurea=2*(formula)
    return(razaoaurea)
    
m=input('Digite o número de m termos da fórmula pi:')
epsilon=input('Digite o epsilon para o cálculo da razão aurea:')

print('%.15f'%(calcula_pi(m)))
print('%.15f'%(calcula_razao_aurea(m,epsilon)))