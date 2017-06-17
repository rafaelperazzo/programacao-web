# -*- coding: utf-8 -*-
#from__future__import division


#Primeiro é necessário calcular o valor absoluto do epsilon,
#ou seja, em módulo
def calcula_valor_absoluto(x):
    if x<0:
        x = x * (-1)
    else:
        x = x * 1
    return(x)

#A função calcula pi incluindo os m primeiros termos começando a contar depois do 3.
def calcula_pi(m):
    soma = 0
    denominador = 2
    for i in range( 1 ,m+1, 1):
        if i%2==1:
            soma = soma + ( 4 / (( denominador ) * ( denominador + 1 ) * ( denominador + 2 )))
        else:
            soma = soma - ( 4 / (( denominador ) * ( denominador + 1 ) * ( denominador + 2 )))
        denominador = denominador + 2
    pi = 3 + ( soma )
    return(pi)
    
#A função fatorial é responsável por calcular o fatorial do denominador 
#na série da função em que iremos aproximar o cosseno. 
def fatorial(n):
    i = 1
    fatorial = 1
    while i<=n:
        fatorial = fatorial * i
        i = i + 1
    return(fatorial)
    

#Usaremos a próxima função para aproximar a função cosseno, da série de potências,
#que incluem a soma de todos os termos que ainda obtiverem o valor absoluto de epsilon.
def calcula_co_seno(z,epsilon):
    expoente = 2
    i = 1
    term o = (( z ** expoente ) / ( fatorial ( expoente ) ))
    soma = 0
    while termo>epsilon:
        if i%2==1:
            soma = soma - termo
        else:
            soma = soma + termo
        i = i + 1
        expoente = expoente + 2
        termo = (( z**expoente ) / ( fatorial ( expoente ) ))
    cosseno = 1 + ( soma )
    return(cosseno)
    

#Por fim, o cáculo da razão áurea.     
def calcula_razao_aurea(m,epsilon):
    formula = calcula_co_seno(( calcula_pi(m) ) / ( 5 ) , epsilon )
    razaoaurea = 2 * ( formula )
    return(razaoaurea)
    

# M e Epsilon representam as entradas em que o usuário comanda.     
m=int(input('Digite o número de m termos da fórmula pi:'))
epsilon=float(input('Digite o epsilon para o cálculo da razão aurea:'))

#Por fim, aqui serão impressos os resultados de pi e da razão áurea para o usuário. 
print('%.15f'%(calcula_pi(m)))
print('%.15f'%(calcula_razao_aurea(m,epsilon)))