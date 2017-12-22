# -*- coding: utf-8 -*-
n = int(input("Digite a quantidade de elementos das listas: "))
while n<=1:
    n = int(input("Digite a quantidade de elementos das listas: "))
a = []
for i in range (0,n,1):
    a.append(int(input("Digite um valor para a lista a: ")))
print("a = " + str (a))
b = []
for i in range (0,n,1):
    b.append(int(input("Digite um valor para a lista b: ")))
print("b = " + str (a))
c = []
for i in range (0,n,1):
    c.append(int(input("Digite um valor para a lista c: ")))
print("b = " + str (a))



#escreva o código da função crescente aqui

a_ordenados = sorted(a)
a_desordenados = reversed(a)
if a == a_ordenados:
    print("S")
    print("N")
elif a == a_desordenados:
    print("N")
    print("S")
else:
    print("N")
    print("N")
b_ordenados = sorted(b)
b_desordenados = reversed(b)
if b == b_ordenados:
    print("S")
    print("N")
elif b == b_desordenados:
    print("N")
    print("S")
else:
    print("N")
    print("N")
c_ordenados = sorted(c)
c_desordenados = reversed(c)
if c == c_ordenados:
    print("S")
    print("N")
elif c == c_desordenados:
    print("N")
    print("S")
else:
    print("N")
    print("N")






#escreva as demais funções





#escreva o programa principal
