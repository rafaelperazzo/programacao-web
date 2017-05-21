def fatorial(n):
    produto=1
    for i in range(1,n+1,1):
        produto=produto*i
    return (produto)
def seno(x,E):
    termo=1
    soma=0
    expoente=1
    while ((x**expoente)/fatorial(expoente))>E:
        if termo%2!=0:
            soma=soma+(x**expoente)/fatorial(expoente)
        else:
            soma=soma-(x**expoente)/fatorial(expoente)
        expoente=expoente+2
        termo=termo+1
    return (soma)
x=float(input('x: '))
E=float(input('E: '))
resultado=seno(x,E)
print(resultado)