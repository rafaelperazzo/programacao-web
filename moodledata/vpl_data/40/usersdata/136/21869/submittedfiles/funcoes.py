#ARQUIVO COM SUAS FUNCOES

def calcula_valor_absoluto(x):
    if x < 0:
        x = x*(-1)
    return x

def calcula_pi(m):
    expr = 0
    x = 2
    for i in range (0, m, 1):
        if 1<=m<=2000: #para m maior ou igual a 1 e menor ou igual a 2000
            if i%2==1: #se i for ímpar
                expr = expr + (4/(x*(x+1)*(x+2)))
            else: #caso contrário
                expr = expr - (4/(x*(x+1)*(x+2)))
        x = x +2
    calcula_pi = 3 + expr #pi será igual a 3 + a expressão final
    
    return calcula_pi #a função retorna o valor de pi

def fatorial(n):
    if n <= 1:
        return 1
    else n*fatorial(n-1)
    
def calcula_co_seno(z, epsilon):
    soma = 0
    i = 1
    expoente = 2
    fracao = (z**expoente)/fatorial(expoente) # observa-se, aqui, que é chamada a função fatorial com o exponte dentro da mesma
    while fracao>epsilon:
        fracao = (z**expoente)/fatorial(expoente)
        if i%2==1:
            soma = soma - fracao
        else:
            soma = soma + fracao
        expoente = expoente + 2
        i = i + 1
    calcula_co_seno = soma + 1
    return calcula_co_seno

def calcula_razao_aurea(m, epsilon):
    fi = 2 * calcula_co_seno(calcula_pi(m)/5, epsilon)
    return fi

