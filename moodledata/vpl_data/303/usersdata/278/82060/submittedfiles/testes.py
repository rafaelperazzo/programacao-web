x1=0
x2=100
soma=0
while (True):
    x1+=1
    if x1>=x2:
        break
    if x1%2==0:
        soma+=x1
print("%.d" %(soma))
    