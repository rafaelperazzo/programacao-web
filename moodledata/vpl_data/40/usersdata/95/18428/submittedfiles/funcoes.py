#ARQUIVO COM SUAS FUNCOES
def fatorial(n):
    produto=1
    for i in range(1,n+1,1):
        produto=produto*i
    return produto

def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
    return x

a=input('A')
print calcula_valor_absoluto(a)