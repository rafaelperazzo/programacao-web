# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
resultado='L' 
while (True) :
 
 import random
 b=0
 a=0
 escolha=['X','O']
 imagem=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
 posicao=[['00','01','02'],['10','11','12'],['20','21','22']]
 sorteio=random.choice(escolha)
 if resultado=='N'  :
   break
 resultado='L'  
 print(sorteio)

 while(True):
  if resultado!='L' :
      break
  simbolo=(input('Qual simbolo deseja utilizar ? '))
  if simbolo=='X' or simbolo=='O':
     break
     
  else:
      print('Digite X ou O ')
 while(True) :
    
  if resultado!='L' :
      break
  while(True):
    if resultado!='L' :
        break
    if sorteio=='O' :
       sorteio='X'
    else:
        sorteio='O'
    if sorteio!=simbolo :
        print(simbolo)
        while(True) :
            if b==0 :
             jogada=((input('Qual sua jogada ')))
            
             for i in range (0,3,1):
              for j in range (0,3,1):
                 
                if jogada==posicao[i][j] :
                   if imagem[i][j]==' ' :
                      
                       
                       a=a+1
                       imagem[i][j]=simbolo
                       
                       b=1
                       for i in range(0,3,1):
                           print('%s|%s|%s'(%imagem[i],%imagem[i+1],%imagem[i+2]))
             for i in range(0,3,1) :
                    if imagem[i][0]==imagem[i][1] and imagem[i][0]==imagem[i][2] :
                        if imagem[i][0]=='X' or imagem[i][0]=='O' :
                         resultado='N'
             for j in range(0,3,1) :
                    if imagem[0][j]==imagem[1][j] and imagem[0][j]==imagem[2][j] :
                        if imagem[0][j]=='X' or imagem[0][j]=='O' :
                         resultado='N'    
             if imagem[0][0]==imagem[1][1] and imagem[0][0]==imagem[2][2] :
                       if imagem[0][0]=='X' or imagem[0][0]=='O' :
                         resultado='N'
             if imagem[0][2]==imagem[1][1] and  imagem[0][2]==imagem[2][0]:
                       if imagem[2][0]=='X' or imagem[2][0]=='O' :
                         resultado='N'
                         
             while(True) :
                if resultado=='N':
                    
                  print('voce venceu')
                  resultado=(input('Deseja continuar S ou N'))
                  if resultado=='S' or resultado=='N' :
                       a=0
                       break            
                  else:
                      resultado='N'
                else:
                    break
            else :
                if a==9 ;
                    print('Deu velha')
                    while(True) :
                     resultado=(input('deseja continuar S ou N '))
                     if resultado=='S' or resultado=='N' :
                         break
                b=0
                break         
                            
    if sorteio==simbolo:
        while(True) :
          if b==0 :  
            jogada2=(random.choice(random.choice(posicao)))
            print(jogada2)
            for i in range (0,3,1):
             for j in range (0,3,1):
                 
                 if (jogada2==posicao[i][j]) :
                   if imagem[i][j]==' ' :
                       a=a+1
                       if sorteio=='X' :
                        b=1   
                        imagem[i][j]='O'
                       else:
                           imagem[i][j]='X'
                           b=1 
            for i in range(0,3,1) :
                    if imagem[i][0]==imagem[i][1] and imagem[i][0]==imagem[i][2] :
                        if imagem[i][0]=='X' or imagem[i][0]=='O' :
                         resultado='N'
            for j in range(0,3,1) :
                    if imagem[0][j]==imagem[1][j] and imagem[0][j]==imagem[2][j] :
                        if imagem[0][j]=='X' or imagem[0][j]=='O' :
                         resultado='N'    
            if imagem[0][0]==imagem[1][1] and imagem[0][0]==imagem[2][2] :
                        if imagem[0][0]=='X' or imagem[0][0]=='O' :
                         resultado='N'
            if imagem[0][2]==imagem[1][1] and  imagem[0][2]==imagem[2][0]:
                        if imagem[2][0]=='X' or imagem[2][0]=='O' :
                         resultado='N'
            while(True) :
                if resultado=='N':
                  print('computador venceu')
                  resultado=(input('Deseja continuar S ou N'))
                  if resultado=='S' or resultado=='N' :
                       a=0
                       break            
                  else:
                      resultado='N' 
                else:
                    break
          else:
            if a==9 :
                print('Deu velha')
                while(True) :
                 resultado=(input('deseja continuar S ou N'))
                 if resultado=='S' or resultado=='N' :
                     break
            b=0
            break  
    break











































 
















    
    
    





