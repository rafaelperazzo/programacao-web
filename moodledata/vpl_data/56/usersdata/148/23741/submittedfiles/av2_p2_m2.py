from __future__ import division

def vidas(a,entrada,saida):
    soma=0
    if entrada>=saida:
        while entrada>=saida:
            soma=soma+a[entrada]
            entrada=entrada-1
    else:
        while saida>=entrada:
            soma=soma+a[saida]
            saida=saida-1
    return soma

n=input('Digite a quantidade de salas:')
a=[]
for i in range(0,n,1):
    a.append(input('Digite um elemento:'))

entrada=input('Digite a porta de entrada:')
saida=input('Digite a porta de saida:')

vidasf=vidas(a,entrada,saida)
print('Vidas: %.f' %vidasf)
