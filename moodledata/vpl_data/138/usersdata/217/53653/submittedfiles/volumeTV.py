v=int(input('Digite o Volume inicial:'))
t=int(input('Digite o numero de Trocas:'))
p=0
while 0<=p and p<=100:
    for i in range(0,t,1):
        ti=float(input('Digite o valor:'))
        if ti>=0:
        p=v+ti
    else:
        p=v-ti
print(p)
  
