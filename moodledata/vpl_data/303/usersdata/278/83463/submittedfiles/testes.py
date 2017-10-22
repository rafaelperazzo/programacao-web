n = int(input("Digite um número não negativo: "))
while  (n<0):
    n = int(input("Digite um número não negativo: "))
f=1
for i in range (0,n+1,1):
    f*=i
print("%.d" %(f))
    