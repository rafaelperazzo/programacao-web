v=int(input('Digite o Volume inicial:'))
t=int(input('Digite o número de trocas:'))
for i in range(0,t,1):
    a=float(input('Digite o Volume:'))
    v=v+a
    if v<0:
        v=0
    elif v>100:
        v=100
print('%.d'%v)