# -*- coding: utf-8 -*-

num= int(input("Digite um algarismo com 8 digitos:"))



K=100000000
b=0
x=0

p=num//K
    
if (p==0 and num!=100000000):
        print ("NAO SEI")

else:
    

        while (x<8):
            f=num%K
            num=num//K
    
    
            K=K/10
            b=b+num
            x=x+1
            num=f
            
    print (" %d " % b) 
