# -*- coding: utf-8 -*-
n=int(input("Digite n: "))
a=[]
b=[]

for i in range (0,n,1):
    a.append(int(input("Digite um valor: ")))

for i in range (0,n,1):
    b.append(int(input("Digite um valor: ")))
    
conta=0
contb=0
#comparações para "a"

if a[0]>a[1]:
    conta=conta+1
if a[n]>a[n-1]:
    conta=conta+1
for i in range (1,n-2,1):
    if a[i]>a[i+1] and a[i]>a[i-1]:
        conta=conta+1

#comparações para "b"

if b[0]>b[1]:
    contb=contb+1
if b[n]>b[n-1]:
    contb=contb+1
for i in range (1,n-2,1):
    if b[i]>b[i+1] and b[i]>b[i-1]:
        contb=contb+1

if conta==1:
    print("S")
if conta != 1:
    print("N")
if contb==1:
    print("S")
if contb != 1:
    print("N")