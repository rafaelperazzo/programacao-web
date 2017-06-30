# -*- coding: utf-8 -*-
'''A razão áurea, também conhecida por proporção áurea é uma constante real irracional obtida pela divisão de uma reta em dois segmentos
de maneira que a divisão do segmento maior pelo menor seja igual a reta completa dividida pelo maior segmento, usualmente arredondada 
para 1,61803398875, denotada pela letra grega PHI. O objetivo do trabalho é criar um programa na linguagem Python usando os conceitos de
funções, estruturas de repetição e variáveis flutuantes.'''
#Primeiro passo é calcular o valor de Pi
def pi (m):
    soma = 3
    x = 2
    y = 3
    z = 4
    for termo in range (1, m+1, 1):
        if termo % 2 == 0:
            soma = soma - (4/(x*y*z))
        else:
            soma = soma + (4/(x*y*z))
        x = x + 2
        y = y + 2
        z = z + 2
    return (soma)
'''Criamos uma função para calcular o valor de Pi, na qual receberá como parâmetro m. A série inicia-se com um somátorio com três como valor
fixo. Além disso, é necessário criar uma repetição para calcular o valor do termo que tem o parâmetro m como critério de parada. O termo 
apresenta no numerador o número fixo quatro, enquanto que o denominador é o produto de três variáveis que são atualizadas acrescentando-se
o número dois. Quando o termo for par, subtrai o seu valor do somatório. Caso contrário, soma.'''
def cosseno (z,epsilon):
    soma=1
    i=2
    fatorial=2
    v=1
    termo=1
    while termo>=epsilon:
        termo=(z**i)/fatorial
        if v%2==0:
            soma=soma+termo
        else:
            soma=soma-termo
        i=i+2
        fatorial=fatorial*(i-1)*i
        v=v+1
    return (soma)
def razaoaurea(m,epsilon):
    razao=2*(cosseno(pi(m)/5,epsilon))
    return(razao)

m=int(input('m:'))
epsilon=float(input('epsilon:'))
print(pi(m))
print(razaoaurea(m,epsilon))