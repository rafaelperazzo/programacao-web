n = int(input("Digite um número não negativo: "))
while  (n<0):
    n = int(input("Digite um número não negativo: "))
f=1
for n in range (1,n+1,1):
    f*=n
print("%.d" %(f))
    