# -*- coding: utf-8 -*-
n1 = int(input('Digite o n min: '))
n2 = int(input('Digite o n max: '))
for x in range(n1,n2+1,1):
	for y in range(n1,n2+1,1):
		 print('(%d,%d) ' % (x,y))














































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
"""
for i in range(0,100,2) :
    if i == 0 :
        continue
    print(i)
"""









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












