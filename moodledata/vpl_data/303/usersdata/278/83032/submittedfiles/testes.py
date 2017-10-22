x = int(input("Digite x: "))
n = float(input("Digite n: "))
def raiz(x,n):
    resultado = x**(1/float(n))
    return resultado
print(raiz(x,n))