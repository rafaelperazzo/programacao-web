x = int(input("Digite um número: "))
d = 2
contador = 0
while (2<(x-1)):
    if x%2==0:
        contador+=1
        d+=1
if contador>0:
    print("%.d não é primo" %(x))
else:
    print("%.d é primo" %(x))
