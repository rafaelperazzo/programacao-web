n=int(input('numero de competidores:'))
p=int(input('nota minima:'))
soma=0
cont=0
for i in range(1,n+1,1):
    x=int(input('primeira nota:'))
    y=int(input('segunda nota:'))
    soma=x+y
    if soma>=p:
        cont=cont+1
print(cont)