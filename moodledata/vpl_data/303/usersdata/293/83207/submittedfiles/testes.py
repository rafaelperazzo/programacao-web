n=int(input("Digite número inteiro não negativo: "))

while n<0 or type(n)==float:
    print("número inválido")
    n=int(input("Digite número inteiro não negativo: "))
print(n)