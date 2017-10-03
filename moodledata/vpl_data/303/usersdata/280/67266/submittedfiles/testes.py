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
metro=float(imput("Medida em metros="))