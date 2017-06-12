n=int(input('Volume inicial:'))
m=int(input('Mudança de volume:'))
soma=n
for i in range(1,m+1,1):
    v=int(input('Alteração do volume:'))
    soma=soma+v
    if soma>100:
        soma=100
    elif soma<0:
        soma=0
print(soma)