# -*- coding: utf-8 -*-
import time

n = int(input('Digite o número de notas: '))
notas  = []

for i in range (0,n,1):
    notas.append(float(input('Digite a nota %d: ' %(i + 1))))

denominador_harmonico = 0

for i in range (0,n,1):
    print("dHM anterior="+str(denominador_harmonico))
    denominador_harmonico += 1.0/notas[i]
    print('FRACAO: 1.0/' + str(notas[i]))
    print("dHM apos soma="+str(denominador_harmonico))
    print(" ")
    time.sleep(10)

media_harmonica = n / denominador_harmonico 
print(media_harmonica)
    
    
    
    
    
    
    
    

#n = ler_inteiro()
#mostrar_na_tela("%d! = %d" % (n,fatorial(n)))