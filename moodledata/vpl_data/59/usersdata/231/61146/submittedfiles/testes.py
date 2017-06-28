# -*- coding: utf-8 -*
n=4
a=[]
for i in range(0,n,1):
    valor=int(input('digite-%d° o elemento de cada indice:'%i))
    a.append(valor)
m=int(str(a[0])+str(a[1])+str(a[2])+str(a[3]))
k=int(str(a[1])+str(a[0]))
l=int(str(a[2])+str(a[3]))
u=int(str(a[2])+str(a[1]))
w=int(str(a[0])+str(a[3]))
g=int(str(a[2])+str(a[0]))
p=int(str(a[1])+str(a[3]))
if m==(k*l):
    print('É NUMERO VAMPIRO')
elif m==(u*w):
    print('É NUMERO VAMPIRO')
elif m==(g*p):
     print('É NUMERO VAMPIRO')
else:
    print('NAO É NUMERO VAMPIRO')
    
    
# Como ja se sabe,so existem sete numeros vampiros de quatro digitos,sendo que
# quatro deles atendem a mesma condição de permutação pra que sejam vampiros,onde
# tal condição é que, inverte o indice[1] com o indice[0] , e o indice[2] e o indice[3]
# permanecem no mesmo lugar, e com isso faz a multiplicação da soma de ambos,so que em forma
# de texto ultilizando para essa transformação a função (str), e depois retornando o
# valor dessa soma para um numero natural inteiro com a função
# (int), fazendo tambem esse mesmo processo para o numero( se é vampiro ou não) dado,
# para poder fazer a comparação de igualdade, entre o numero dado e a multiplicação
# entre as permutações, pois se ambos forem iguais o numero sera vampiro, se não,
# não sera vampiro. Faz-se o mesmo para as outras condições onde invertice o indice[2]
# com o indice[1] e faz a soma de ambos e depois a multiplição dessa soma pela a soma
# do indice[0] + o indice[3], e a ultima condição é que, inverte o indice[2] com o indice[0]
# faz a soma, e multiplica por a soma do indice[1] +  indice[3], logo todos os numeros vampiros
# atenderam a essas condições.
 

    
   
        
    
