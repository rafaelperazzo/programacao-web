n = int(input("Digite um número não negativo: "))
while  (n<0):
    n = int(input("Digite um número não negativo: "))
f=1
while (n>0):
    f=1*n
    n=n-1
    return f
print(f)
    