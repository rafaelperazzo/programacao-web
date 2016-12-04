#ARQUIVO COM SUAS FUNCOES
#Estabelecer a função valor_absoluto para comparar o valor do cosseno com o epislon
def valor_absoluto(x):
    if x>=0:
        valorabsoluto = x
    else:
        valorabsoluto = x*(-1)
    return valorabsoluto

#calculo do valor de pi
def calcula_pi(m):
    pi = 3.00
    a=2.00
    variavel =1
    i=1
    while i<= m:
        pi = pi + ((variavel*4)/(a*(a+1)*(a+2)))
        a = a+2
        variavel = variavel*(-1)
        i=i+1
    return pi

#Para calcular a função cosseno, é necessário definir a função fatorial para os denominadores
def fatorial(a):
    fatorial = 1
    while a>=1:
        fatorial = fatorial*a
        a = a-1
    return fatorial
    
#Iniciarei o cosseno com cosz=1 para facilitar os cálculos, já que é a parte fixa para o cálculo de todos os cossenos
#criei uma variável p para facilitar no fator de correção do sinal
def calcula_co_seno(x,epislon):
    cosz = 1.00
    p = 1.00
    while True:
        cosz = cosz+((((x**2)**p)/fatorial(2*p))*((-1)**p))
        if valor_absoluto ((((x**2)**p)/fatorial(2*p))*((-1)**p)) > epislon:
            p = p+1
        else:
            break
    return cosz
    
def razao_aurea(m,epislon):
    z = (calcula_pi(m)/5)
    RA = 2*calcula_co_seno(z,epislon)
    return RA
    
print calcula_co_seno(20,0.0004)
print razao_aurea(100,0.000001)
p=2
x=2
soma= fatorial(2*p)
soma1= ((((x**2)**p)/fatorial(2*p))*((-1)**p))
print soma
print soma1
