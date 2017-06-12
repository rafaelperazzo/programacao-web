v=int(input('Digite o Volume inicial:'))
t=int(input('Digite o numero de Trocas:'))
for i in range(0,t,1):
    a=float(input('Digite o valor:'))
    v=v+a
    if v<0:
        v=0
    elif v>100:
        v=100
print(v)
  
