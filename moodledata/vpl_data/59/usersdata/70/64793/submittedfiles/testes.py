# -*- coding: utf -8-*
import random

x = range(100)
random.shuffle(x)

while(True):
    num = input("Digite o valor: ")
    
    if(num == x[0]):
        print("Voce acertou o numero: "),num
        break
    else:
        if(num > x[0]):
            print ("o numero é menor")
        else:
            print ("o numero é maior")
            
raw_input("...")
