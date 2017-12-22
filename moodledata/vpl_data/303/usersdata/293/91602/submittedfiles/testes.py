
n=int(input("Digite número inteiro não negativo: "))
fatorial=1
while n<0  :
    print("número inválido")
    n=int(input("Digite número inteiro não negativo: "))

for i in range(n,0,-1):
    fatorial=fatorial*i
print("%d! = %d" %(n,fatorial))