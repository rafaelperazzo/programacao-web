# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
c1 = int(input("Digite o valor da primeira carta: "))
c2 = int(input("Digite o valor da segunda carta: "))
c3 = int(input("Digite o valor da terceira carta: "))
c4 = int(input("Digite o valor da quarta carta: "))
c5 = int(input("Digite o valor da quinta carta: "))
c6 = int(input("Digite o valor da sexta carta: "))
if 1<=c1<=13 and 1<=c2<=13 and 1<=c3<=13 and 1<=c4<=13 and 1<=c5<=13 and 1<=c6<=13: 
    if c1<c2 and c2<c3 and c3<c4 and c4<c5 and c5<c6:
        if c1!=c2 and c2!=c3 and c3!=c4 and c4!=c5 and c5!=c6:
            print("C")
elif c1<c2 and c2<c3 and c3<c4 and c4<c5 and c5<c6:
else:
    print("N")
if 1<=c1<=13 and 1<=c2<=13 and 1<=c3<=13 and 1<=c4<=13 and 1<=c5<=13 and 1<=c6<=13:  
    if c1>c2 and c2>c3 and c3>c4 and c4>c5 and c5>c6:
        if c1!=c2 and c2!=c3 and c3!=c4 and c4!=c5 and c5!=c6:
             print ("D")
elif c1>c2 and c2>c3 and c3>c4 and c4>c5 and c5>c6:
else:
    print("N")
        print ("N")
                    
        
        

      
 
   
    