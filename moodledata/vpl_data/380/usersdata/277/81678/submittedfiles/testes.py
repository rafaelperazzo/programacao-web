# -*- coding: utf-8 -*-
#print "hello"

"""
# ENTRADA 
x = int(input('digite um numero inteiro qualquer: '))

# PROCESSAMENTO 
teste1 = x > 50
teste2 = (x > 0) and (x <= 100)

# SAIDA 
print("O numero " + str(x) + " é maior do que 50: " + str(teste1)) 
print("O numero " + str(x) + " está entre 0 e 100: " + str(teste2))

"""

n = -1
x = -1
validou = False
while (not validou):
    validouInput1 = False
    while (n < 1 or n > 13):
        n = int(input('Digite o valor da carta [1,13]: '))
    validouInput1 = True
    validouInput2 = False
    while (x < 10 or x > 99):
        n = int(input('Digite o numero da aposta [10,99]: '))
    validouInput2 = True
    validou = validouInput1 and validouInput2









"""
# ENTRADA
n1 = float(input('Nota B1: '))
n2 = float(input('Nota B2: '))
n3 = float(input('Nota B3: '))
n4 = float(input('Nota B4: '))

# PROCESSAMENTO
media = (n1 + n2 + n3 + n4) / 4

# SAIDA
print('%.2f' % media)
"""

"""
# ENTRADA
medida = float(input("digite um valor em metros: "))
# PROCESSAMENTO
conversao = medida * 100
# SAIDA
print("%.2f metros = %d centimetros" % (medida, conversao) )
"""












