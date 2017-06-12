n=int(input('inicial:'))
m=int(input('alteração:'))
soma=n
for i in range(1,m+1,1):
    v=int(input('digite alteração vol:'))
    soma=soma+v
    if soma>100:
        soma=100
    if soma<0:
        soma=0
print(soma)