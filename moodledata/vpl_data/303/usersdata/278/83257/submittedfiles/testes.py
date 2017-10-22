n = int(input("Digite um número não negativo: "))
while  (n<0):
    n = int(input("Digite um número não negativo: "))
f=1
i=0
for n in range (0,n,-1):
    while (n>=i):
        f=1*n
        i=+1
print(f)
    