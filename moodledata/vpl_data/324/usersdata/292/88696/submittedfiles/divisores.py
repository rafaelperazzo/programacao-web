# -*- coding: utf-8 -*-

def multiplos(n, a, b):
    mult_a, mult_b, mult_a_b, cont = [], [], [], 0
    for i in range(1, n+1):
        mult_a.append(i*a)
        mult_b.append(i*b)
    
    mult_a_b = mult_a + mult_b
    mult_a_b.sort()
    while cont < 6:
        print(mult_a_b[cont])
        cont +=1
        
n = int(input("Digite o número de múltiplos que deseja imprimir: "))
while True:
    if n>0:
        break
    n = int(input("\nNão se imprime %d múltiplos! Digite novamente: "%n))
    
a = int(input("Digite o primeiro número: "))
while True:
    if a>0:
        break
    a = int(input("\nNão se imprimem múltiplos de %d! Digite novamente: "%a))
    
b = int(input("Digite o segundo número: "))
while True:
    if b>0:
        break
    b = int(input("\nNão se imprimem múltiplos de %d! Digite novamente: "%b))
    
multiplos(n, a, b)