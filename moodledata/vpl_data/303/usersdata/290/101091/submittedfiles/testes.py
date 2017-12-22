# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=[0,1,2,3,4,5,6]
for i in range(n,-1,-1):
    
b=[[1,1],[2,2]]
print(a-b)
a=[
    [1,2,3,4,5],
    [2,3,2,5,2]
    ]
print(sum(a[0]))
print(a[0][0])
def pote(a1,e1):
    pot=a1**e1
    return pot
print(pote(3,4))

a=[1,2,6,4]
d=a.reverse()
print(a)
print(d)
a.sort()
print(a)

n=int(input("Digite o valor de n: "))
lista=[]
for i in range(0,n,1):
    lista.append(float(input("Digite o valor: ")))
m=sum(lista)/float(len(lista))
s=0
for i in range(0,n,1):
    s+=((lista[i]-m))**2
d=((1/(n-1))*s)**1/2
print(d)
cont1=0
cont2=0
cont3=0
for i in range(0,n,1):
    if (m-lista[i])<d:
        cont1=cont1+1
    if (m-(lista[i]))<2*d:
        cont2+=1
    if (m-(lista[i]))<3*d:
        cont3+=1


p1=(cont1/float(len(lista)))
p2=(cont2/float(len(lista)))
p3=(cont3/float(len(lista)))

if p1>=(68/100) and p2>=(95/100) and p3>=(99.7/100) :
    print("Distribuição Normal")
else:
    print("Não é uma distribuição Normal")

        
    
    

    
n=int(input("Digite a quantidade de elementos: "))
a=[]
for i in range(0,n,1):
    a.append(int(input("Digite um valor: ")))
for i in range(0,n,1):
    if a[i]%2==0:
        print(a[i])










notas=[]
n=int(input("Digite o número de notas: "))
while n<1:
    n=int(input("Digite o número de notas: "))
for i in range(0,n,1):
    notas.append(float(input("Digite a nota %d: " %(i+1))))
media=0
for i in range(0,n,1):
    media+=notas[i]/n
print(notas)
print(media)



print("__________________________________________")



for i in range(2,3,1):
    print(i)




def misterio(x):
    cont=0
    for i in range(2,x,1):
        if x%i==0:
            cont=cont+1
            break
        if cont==0:
            return True
        else:
            return False
y=30
for i in range(1,y,1):
    if misterio(i):
        print(i)


a=2
b=3
c=5
def funcao(a,b,c):
    if (a+b)==c:
        return true
    else:
        return false
print("___________________________________")

print(5==6)
from minha_bib import *
print(fatorial(5))
print(s(5))

print("___________________________________")

base=float(input("Digite o valor da base: "))
expoente=float(input("Digite o valor do expoente: "))
produto=1
cont=0
while cont<expoente:
    produto=produto*base
    cont+=1
print(produto)

print("___________________________________")
n=float(input("Digite o valor da n: "))
fatorial=1
cont=1
while cont<n+1:
    fatorial=fatorial*cont
    cont+=1
print(fatorial)


n=int(input("Digite o valor de n: "))
for i in range(n):
    print(i)

print("___________________________________")

n=int(input("Digite o valor de n: "))
f=1
for i in range(n,0,-1):
    f=f*i
print(f)

print("___________________________________")
a=float(input("Digite o valor da base: "))
x=float(input("Digite o valor do expoente: "))
cont=0
produto=1
while cont<x:
    produto=produto*a
    cont+=1
print(a, "elevado a", x, "=", produto)

print("___________________________________")
a=int(input("Digite o valor de a: "))
i=1
b=0
while b<a:
    i=i
print("___________________________________")

i=0
while i<10:
    print(i)
    i+=1
from minha_bib import *
print(fatorial(5))

cronometro(5)
#helo_world()

