
v=int(input('Digite o volume incial:'))
t=int(input('digite o numero de mudanças de volume:'))
volume=v
cont=0
for i in range (1,t+1,):
    a=int(input('Digite a mudança de volume:'))
    volume=volume+a
    if (volume>100):
        volume=100
    if (volume<0):
        volume=0
print(volume)