# -*- coding: utf-8 -*-
a1=int(input('Digite o primeiro número escolhido:'))
a2=int(input('Digite o segundo número escolhido:'))
a3=int(input('Digite o terceiro número escolhido:'))
a4=int(input('Digite o quarto número escolhido:'))
a5=int(input('Digite o quinto número escolhido:'))
a6=int(input('Digite o sexto número escolhido:'))
s1=int(input('Digite o primeiro número sorteado:'))
s2=int(input('Digite o segundo número sorteado:'))
s3=int(input('Digite o terceiro número sorteado:'))
s4=int(input('Digite o quarto número sorteado:'))
s5=int(input('Digite o quinto número sorteado:'))
s6=int(input('Digite o sexto número sorteado:'))
i=1
contador=0
for i in range(1,100,1):
    if i%s1==1 and i%s2==1 and i%s3==1 and i%s4==1 and i%s5==1 and i%s6==1:
        print('sena')
