n=int(input("Digite número inteiro não negativo: "))

while n<0 or float(n):
    print("número inválido")
    n=int(input("Digite número inteiro não negativo: "))
print(n)