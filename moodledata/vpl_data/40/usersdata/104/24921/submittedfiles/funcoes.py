def fatorial(n):
    f=1
    for i in range(1,n+1,1):
        f=f*i
    return f
def calcula_valor_absoluto(x):
    if x>=0:
        return (x)
    else:
        return (-x)

print calcula_valor_absoluto(5)