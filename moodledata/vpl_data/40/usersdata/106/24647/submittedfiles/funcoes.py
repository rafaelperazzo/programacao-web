#ARQUIVO COM SUAS FUNCOES
def valor_absoluto(x):
    if x>=0:
        valorabsoluto = x
    else:
        valorabsoluto = x*(-1)
    return valorabsoluto

def calcula_pi(m):
    Soma = 3
    a=2
    for i in range (0,m,1):
        Soma = Soma + (4*((-1)**i))/(a*(a+1)*(a+2))
        a = a+2
    return Soma

def fatorial(a):
    fatorial = 1
    while a>=1:
        fatorial = fatorial*a
        a = a-1
    return fatorial
    
def calcula_co_seno(x,epislon):
    cosz = 1
    p = 1
    while True:
        cosz = cosz+((((x**2)**p)/fatorial(2*p))*((-1)**p))
        if valor_absoluto ((((x**2)**p)/fatorial(2*p))*((-1)**p)) > epislon:
            p = p+1
        else:
            break
    return cosz
    
def razao_aurea(m,epislon):
    RA = 2*calcula_co_seno(((calcula_pi(m))/5),epislon)
    return RA
    
print (valor_absoluto(-10))
print('%.15f' %calcula_pi(100))
print (fatorial (5))
print calcula_co_seno(20,0.0004)
print razao_aurea(100,0.0004)