#coding: utf-8
n=int(input('digite n: '))
soma=3
v1=2
v2=3
v3=4
for i in range(1,n+1,1):
    if i%2==0:
        soma=soma-4/(v1*v2*v3)
    else:
        soma=soma+4/(v1*v2*v3)
    v1=v1+1
    v2=v2+1
    v3=v3+1
print(soma)