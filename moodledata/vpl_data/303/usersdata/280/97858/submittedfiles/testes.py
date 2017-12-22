"""
valor=["X","O"]
symh=valor[0]
sympc=valor[1]
print(symh)
print(sympc)
line1=[" "," "," "]
line2=[" "," "," "]
line3=[" "," "," "]   
print("|%s|%s|%s|" % (line1[0],line1[1],line1[2]) )
print("|%s|%s|%s|" % (line2[0],line2[1],line2[2]) )   
print("|%s|%s|%s|" % (line3[0],line3[1],line3[2]) )
line1[2]=symh
print("|%s|%s|%s|" % (line1[0],line1[1],line1[2]) )
print("|%s|%s|%s|" % (line2[0],line2[1],line2[2]) )   
print("|%s|%s|%s|" % (line3[0],line3[1],line3[2]) )
line2[1]=sympc
print("|%s|%s|%s|" % (line1[0],line1[1],line1[2]) )
print("|%s|%s|%s|" % (line2[0],line2[1],line2[2]) )   
print("|%s|%s|%s|" % (line3[0],line3[1],line3[2]) )
line3[2]=symh
print("|%s|%s|%s|" % (line1[0],line1[1],line1[2]) )
print("|%s|%s|%s|" % (line2[0],line2[1],line2[2]) )   
print("|%s|%s|%s|" % (line3[0],line3[1],line3[2]) )
"""
"""
x=int(input("Número de médias: "))
while x <= 1:
    x=int(input("Número de médias: "))
notas=[]
for i in range (0,x,1):
    notas.append(float(input("Insira a nota %d: " %(i+1))))
soma=sum(notas)
res=soma/x
print(res)
"""
"""
n=int(input("Insira n: "))
a=[]
for i in range (0,n,1):
    a.append(int(input("Digite o termo %d do vetor a: " %(i+1))))
med=sum(a)/len(a)
somat=0
for i in range (0,len(a),1):
    somat=somat + ((a[i]-med)**2)
desvpad=(((1/(n-1))*(somat))**0.5)
print(desvpad)    
"""
import numpy as np

dim=int(input("Dimensão n da matriz: "))
matriz=np.empty[dim,dim]
for i in range (0,dim,1):
    for j in range (0,dim,1):
        matriz[i][j]=float(input("Digite o nº da linha %d na coluna %d: " %(i+1),(j+1)))
print(matriz)
if sum(matriz[0]) == sum(matriz[


    

print(matriz)

