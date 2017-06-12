v=int(input('Digite o Volume inicial:'))
t=int(input('Digite o numero de Trocas:'))
while 0<=v and v<=100:
    for i in range(0,t,1):
        ti=float(input('Digite o valor:'))
        if ti>=0:
        v=v+ti
    else:
        v=v-ti
print(v)
  
