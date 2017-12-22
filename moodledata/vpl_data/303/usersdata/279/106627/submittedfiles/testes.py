# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
while (True) :
 if resultado=='N' :
   break
 import random
 b=0
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
    

  if resultado=='N' :
      break
  while(True):
    if sorteio=='O' :
       sorteio='X'
    else:
        sorteio='O'
    if sorteio!=simbolo :
        print(simbolo)
        while(True):
            if b==0 :
             jogada=((input('Qual sua jogada ')))
            
             for i in range (0,3,1):
              for j in range (0,3,1):
                 
                if jogada==posicao[i][j] :
                   
                   if imagem[i][j]==' ' :
                      
                       
                       a=a+1
                       imagem[i][j]=simbolo
                       
                       b=1
             
            else :
                b=0
                print(imagem)
                break
            if resultado=='S' :
                for i in range(0,3,1) :
                    if imagem[i][0]==imagem[i][1] and imagem[i][0]==imagem[i][2] :
                      if imagem [i][0]=='X' or imagem [i][0]=='O' :
                       if imagem[i][0]==simbolo :   
                        
                        resultado='N'
                for j in range(0,3,1) :
                    if imagem[0][j]==imagem[1][j] and imagem[0][j]==imagem[2][j] :
                      
                       if imagem[i][0]==simbolo :   
                        
                        resultado='N'    
                if imagem[0][0]==imagem[1][1] and imagem[0][0]==imagem[2][2] :
                        resultado='N'
                if imagem[0][2]==imagem[1][1] and  imagem[0][2]==imagem[2][0]:
                        resultado='N'
            while(True) :
                if resultado=='N':
                  print('voce venceu')
                  resultado=(input('Deseja continuar S ou N'))
                  if resultado=='S' or resultado=='N' :
                       break            
                  else:
                      resultado='N'
                            
    if sorteio==simbolo:
        while(True) :
          if b==0 :  
            jogada2=(random.choice(random.choice(posicao)))
            print(jogada2)
            for i in range (0,3,1):
             for j in range (0,3,1):
                 
                 if (jogada2==posicao[i][j]) :
                   print('3')
                   print(imagem[i][j])
                   if imagem[i][j]==' ' :
                       
                       print('4')
                       a=a+1
                       if sorteio=='X' :
                        b=1   
                        imagem[i][j]='O'
                       else:
                           imagem[i][j]='X'
                           b=1 
                       
                
                         
          
            if resultado=='S' :
                for i in range(0,3,1) :
                    if imagem[i][0]==imagem[i][1] and imagem[i][0]==imagem[i][2] :
                        resultado='N'
                for j in range(0,3,1) :
                    if imagem[0][j]==imagem[1][j] and imagem[0][j]==imagem[2][j] :
                        resultado='N'    
                if imagem[0][0]==imagem[1][1] and imagem[0][0]==imagem[2][2] :
                        resultado='N'
                if imagem[0][2]==imagem[1][1] and  imagem[0][2]==imagem[2][0]:
                        resultado='N'
            while(True) :
                if resultado='N':
                  print('computador venceu')
                  resultado=(input('Deseja continuar S ou N'))
                  if resultado=='S' or resultado=='N' :
                       break            
                  else:
                      resultado='N'  
           else:
            b=0 
            print(imagem)
            print(jogada2)
            break  
    break











































 
















    
    
    





