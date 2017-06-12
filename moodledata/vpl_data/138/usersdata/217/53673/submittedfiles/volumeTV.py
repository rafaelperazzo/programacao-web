v=int(input('Digite o Volume inicial:'))
t=int(input('Digite o numero de Trocas:'))
e=v
for i in range(0,t,1):
    a=float(input('Digite o valor:'))
    e=e+a
    if e<0:
        e=0
    elif e>100:
        e=100
print(e)
  
