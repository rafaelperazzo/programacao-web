 n=int(input('digite vinicial:'))
 m=int(input('digite mudança:'))
 soma=n
 for i in range(1,m+1,1):
    v=int(input('digite alteração:'))
    soma=soma+v
    if soma>100:
         soma=100
    elif soma<0:
        soma=0
print(soma)