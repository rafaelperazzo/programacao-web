n=int(input('igite '))
j=int(input('igite '))
a=[ ]
for i in range(1,n+1,1):
    valor=float(input('valor '))
    a.append(valor)

b=[ ]
for i in range(1,j+1,1):
    valor=float(input('valor '))
    b.append(valor)
cont=0
for i in range(1,len(a),1):
    for j in range(0,len(b),1):
        if a[i]==b[j]:
            cont=cont+1
print(cont)