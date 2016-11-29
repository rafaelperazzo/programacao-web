#ARQUIVO COM SUAS FUNCOES

def calcula_valor_absoluto(x):
    if x < 0:
        x = x*(-1)
    return x
    
def fatorial(n):
    if n <= 1:
        return 1
    else n*fatorial(n-1)
    
def calculo_cos(x):
    expr = 0
    for i in range (0, 
def calcula_pi(m):
    expr = 0
    x = 2
    for i in range (0, m, 1):
        for 1<=m<=2000: #para m maior ou igual a 1 e menor ou igual a 2000
            if i%2==1: #se i for ímpar
                expr = expr + (4/(x*(x+1)*(x+2)))
            else: #caso contrário
                expr = expr - (4/(x*(x+1)*(x+2)))
        x = x +2
    calcula_pi = 3 + expr #pi será igual a 3 + a expressão final
    
    return calcula_pi #a função retorna o valor de pi

def calcula_co_seno(z, epsilon)

def calcula_razao_aurea(m, epsilon)

print calcula_pi(m)
