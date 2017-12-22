# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import random

a=0
resultado='S'
escolha=['X','O']
imagem=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
posicao=[['00','01','02'],['10','11','12'],['20','21','22']]
while(True):
  simbolo=(input('Qual simbolo deseja utilizar ? '))
  if simbolo=='X' or simbolo=='O':
     break
  else :
      print('Digite X ou O ')
      
sorteio=random.choice(escolha)
print(sorteio)

while(True):
    if sorteio==simbolo :
        print(sorteio)
        while(True):
            jogada=((input('Qual sua jogada ')))
            
            for i in range (0,3,1):
             for j in range (0,3,1):
                 
                if jogada==posicao[i][j] :
                   print('1')
                   if imagem[i][j]==' ' :
                       print('2')
                       a=a+1
                       imagem[i][j]=sorteio
                       break
             break      
            if sorteio=='O' :
             sorteio='X'
           
            else:
             sorteio='O'
            break
    if sorteio!=simbolo:
        while(True) :
            jogada=(random.choice(random.choice(posicao)))
            print(jogada)
            for i in range (0,3,1):
             for j in range (0,3,1):
                 
                 if (jogada==posicao[i][j]) :
                   print('3')
                   if imagem[i][j]==' ' :
                       print('4')
                       a=a+1
                       imagem[i][j]=sorteio
                       print(imagem[i][j])
                       print(jogada)
                       break
                   else:
                     continue
                 else:
                     continue
             break      
            if sorteio=='O' :
             sorteio='X'
           
            else:
             sorteio='O'
            break      











































 
















    
    
    





