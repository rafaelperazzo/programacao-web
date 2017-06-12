v=int(input('Digite o Volume inicial:'))
t=int(input('Digite o numero de Trocas:'))
vf=0
for i in range(0,t,1):
    ti=float(input('Digite o valor:'))
    v1=v+ti
    vf=v1+ti
print(v1)