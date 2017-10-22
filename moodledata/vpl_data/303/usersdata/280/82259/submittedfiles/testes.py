# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
"""
Aula de python (04/09)
"""
"""
print ("Hello World")
print ("Olá\nMundo")
print ("Antônio Marcos Cruz da Paz")
print ("18")
a=11
b=1037
print (a+b)
a=35
print ((9*a+160)/5)
h=30
d=10
print (3.14159*((d/2)**2)*h)
a=2
b=5
print ((2+5)**2)
"""
"""
Programa para medir a média
e dar o resultado final.
"""
"""
print("Bem vindo ao programa para definição de resultado final")
print("Esse programa só aceita notas entre 0 e 10")
print("---------------------------------------------------------")
x=float(input ("Primeira Nota="))
if (x>10):print("Atenção:Insira uma nota válida")
if (x<0):print("Atenção:Insira uma nota válida")
y=float(input ("Segunda Nota="))
if (y>10):print("Atenção:Insira uma nota válida")
if (y<0):print("Atenção:Insira uma nota válida")
z=float((x+y)/2)
print("---------------------------------------------------------")
print ("Nota Final:")
print (z)
print ("Resultado Final:")
if (z<7):print("Reprovado")
if (z>7):print("Aprovado")
if (z==7):print("Aprovado")
"""
"""
nome=str(input("Qual o seu nome?: ")
idade=float(input("Qual é a sua idade?: "))
altura=float(input("Qual é a sua altura?: "))
print ("A idade de +nome+ é %.d e sua altura é %.2f" %(idade,altura))
"""
"""
print("Bem vindo ao programa para definição de resultado final")
print("Esse programa só aceita notas entre 0 e 10")
print("---------------------------------------------------------")
x=float(input ("Primeira Nota="))
if (x>10):print("Atenção:Insira uma nota válida")
if (x<0):print("Atenção:Insira uma nota válida")
y=float(input ("Segunda Nota="))
if (y>10):print("Atenção:Insira uma nota válida")
if (y<0):print("Atenção:Insira uma nota válida")
a=float(input("Terceira Nota="))
if (a>10):print("Atenção:Insira uma nota válida")
if (a<0):print("Atenção:Insira uma nota válida")
b=float(input("Quarta Nota="))
if (b>10):print("Atenção:Insira uma nota válida")
if (b<0):print("Atenção:Insira uma nota válida")
z=float((x+y+a+b)/4)
print("---------------------------------------------------------")
print ("Nota Final:")
print (z)
print ("Resultado Final:")
if (z<7):print("Reprovado")
if (z>7):print("Aprovado")
if (z==7):print("Aprovado")
print("--------------------------------------------------")
m=float(input("Medida em metros="))
cent=float(m*100)
print(cent)
print("--------------------------------------------------")
ah=(float(input("Qual sua altura?: ")))
pes=((72.7*ah)-58)
print(pes)
print("--------------------------------------------------")
rad=(float(input("Valor do raio= ")))
area=(float(3.1416*(rad**2)))
print(area)
print("--------------------------------------------------")
"""
"""
print(bool(not(10<20)))
t1=input("Digite algo: ")
t2=input("Digite algo: ")
t3=input("Digite algo: ")
print(t1+t2+t3)
"""
"""
n1=float(input("n1: "))
n2=float(input("n2: "))
n3=float(input("n3: "))
total=(n1+n2+n3)
print(total)
"""
"""
p=float(input("Insira P: "))
i=float(input("Insira i: "))
n=float(input("Insira n: "))
v=p*((((1+i)**n)-1)/i)
print("%.2f" %v)
"""
"""
a=int(input("Que horas são? [0-23] "))
if a > 3 and a < 12: 
    print ("Bom dia")
elif a >= 12 and a < 18: 
    print ("Boa tarde")
elif a >= 0 and a < 24: 
    print ("Boa noite")
else:
    print ("Entrada inválida")
"""
"""
x1=int(input("x1: "))
x2=int(input("x2: "))
p=0
while (x1 < x2):
    if x1%2 == 0:
        p=p+x1
        print (x1)
    x1 += 1
print (p)
"""
"""
programa FODA para descobrir se um número é primo,
e descobrir seus divisores perfeitos.
"""
"""
x=int(input("Digite o número: "))
c=0
i=2
if x!=0 and x!=1:
    print ("1")
    while i < (x-1):
        if x%i == 0:
            print (i)
            c=c+1
        i += 1
    print (x)
    if c>0:
        print("Não é primo")
    else:
        print("É primo")
else:
    print ("Esse aí é outra história...")
"""
"""
soma = 0
for i in range (0,101,2):
    soma += i
print (soma)
"""

for x in range (-4,5,1):
    for y in range (-4,5,1):
        print('(%d,%d)' %(x,y))

    
    

    