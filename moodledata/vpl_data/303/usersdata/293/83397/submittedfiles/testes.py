n=int(input("Digite número inteiro não negativo: "))
fatorial=1
while n<0  :
    print("número inválido")
    n=int(input("Digite número inteiro não negativo: "))

for n in range(n,0,-1):
    fatorial=fatorial*n
print(fatorial)