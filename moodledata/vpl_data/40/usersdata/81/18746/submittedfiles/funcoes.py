def fatorial(n):
    n_fat=1
    for i in range(1,n+1,1):
        n_fat*=n
        return n_fat

def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
    return x
