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

def pi(m):
    soma=0
    j=2
    for i in range(1,m+1,1):
        if i%2==0:
            soma=soma-(4/(j*(j+1)*(j+2)))
        else:
            soma=soma+(4/(j*(j+1)*(j+2)))
        j=j+2
    soma=soma+3
    return soma

cos=1-soma
m=input('m')
z=pi(m)
print cos
i=0    
while i<m:
    if i%2==0:
        soma=soma-(((z**j)/fatorial(j)))
    else:
        soma=soma +(((z**j)/fatorial(j)))
    j=j+2
    i=i+1
print cos