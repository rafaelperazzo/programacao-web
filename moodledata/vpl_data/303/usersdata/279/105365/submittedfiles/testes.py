# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import random

a=0
resultado='S'
escolha=['X','O']
imagem=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
posicao=[['00','01','02'],['10','11','12'],['20','21','22']]
sorteio=random.choice(escolha)

print(sorteio)

while(True):
  simbolo=(input('Qual simbolo deseja utilizar ? '))
  if simbolo=='X' or simbolo=='O':
     break
     
  else:
      print('Digite X ou O ')
while(True) :
 


 while(True):
    if sorteio=='O' :
       sorteio='X'
    else:
        sorteio='O'
    if sorteio!=simbolo :
        print(simbolo)
        while(True):
            jogada=((input('Qual sua jogada ')))
            
            for i in range (0,3,1):
             for j in range (0,3,1):
                 
                if jogada==posicao[i][j] :
                   
                   if imagem[i][j]==' ' :
                      
                       print(imagem)
                       a=a+1
                       imagem[i][j]=sorteio
                       print(imagem[i][j])
                   
            
            break
    if sorteio==simbolo:
        while(True) :
            jogada2=(random.choice(random.choice(posicao)))
            print(jogada2)
            for i in range (0,3,1):
             for j in range (0,3,1):
                 
                 if (jogada2==posicao[i][j]) :
                   print('3')
                   print(imagem[i][j])
                   if imagem[i][j]==' ' :
                       print(imagem[i][j])
                       print('4')
                       a=a+1
                       imagem[i][j]=sorteio
                       print(imagem[i][j])
                       print(jogada2)
                       break
                  
             break      
        
            break
    break












































 
















    
    
    





