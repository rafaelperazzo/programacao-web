m=int(input('Digite o número m de termos da fórmula pi:'))
epsilon=int(input('Digite o epsilon para o cálculo da razão áurea:'))

def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
    return (x)

def calcula_pi(m):
    pi=3
    y=2
    for i in range(1,m+1,1):
        if i%2==0:
            pi=pi-((4)/(y*(y+1)*(y+2)))
        else:
            pi=pi+((4)/(y*(y+1)*(y+2)))
        y=y+2
    return(pi)
    
calcula_fatorial(m):
    i=1
    fatorial=1
    while i<=m:
        fatorial=fatorial*i
        i=i+1
    return(fatorial)

calcula_co_seno(m,pi):
    soma=1
    numerador=pi
    denominador=2
    if i%2==0:
        soma=soma+(pi**denominador/(fatorial(denominador)))
    else:    
        soma=soma-(pi**denominador/(fatorial(denominador)))
        
print('%.15f' %calcula_pi(m))        
