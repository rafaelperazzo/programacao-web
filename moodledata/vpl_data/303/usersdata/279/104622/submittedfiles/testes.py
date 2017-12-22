# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import random
ids =[0,8]
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
        while(True):
            jogada=(int(input('Qual sua jogada ')))
            for i in range (0,3,1):
             for j in range (0,3,1):
                 if jogada==posicao[i][j] :
                   if imagem[i][j]==" " :
                       a=a+1
                       break
                       break
                       break
                   




























































    
    
    





