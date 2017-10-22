
while(True):
    n = int(input("Digite um numero inteiro positivo: "))
    if (n >= 0) :
        break

fatorial = 1
for i in range(2,n+1,1) :
    fatorial *= i

print("%d! = %d" % (n,fatorial))