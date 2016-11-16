#ARQUIVO COM SUAS FUNCOES
def fatorial(n):
    produto=1
    for i in range(1,n+1,1):
        produto=produto*i
    return produto

a=input('a:')
print fatorial(a)