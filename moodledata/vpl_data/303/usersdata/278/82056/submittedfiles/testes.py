x1 = 0
x2 = 100
soma = 0
x1+=1
while (x1<=x2):
    if x1%2==0:
        soma+=x1
    x1+=1
print("%.d" %(soma))
print("\n")
x1=0
x2=100
soma=0
while (true):
    x1+=1
    if x1>=x2:
        break
    if x1%2==0:
        soma+=x1
print("%.d" %(soma))
    