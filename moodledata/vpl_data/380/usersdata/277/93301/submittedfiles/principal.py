# -*- coding: utf-8 -*-
n = int(input('Digite o número de notas: '))
notas  = []

for i in range (0,n,1):
    notas.append(float(input('Digite a nota %d: ' %(i + 1))))

denominador_harmonico = 0

for i in range (0,n,1):
    denominador_harmonico += 1.0/notas[i]

media_harmonica = n / denominador_harmonico 
print(media_harmonica)
    
    
    
    
    
    
    
    

#n = ler_inteiro()
#mostrar_na_tela("%d! = %d" % (n,fatorial(n)))