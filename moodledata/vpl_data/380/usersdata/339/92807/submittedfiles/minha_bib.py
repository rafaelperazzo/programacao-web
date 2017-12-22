# -*- coding: utf-8 -*-
def ImprimeCampo(campo):
    c=0
    for i in campo:
        if c%3==0:
            print("")
        print (i),
        c+=1
    print("\n")

def ganhou(simbolo, campo):
    if campo[0]==simbolo and campo[1]==simbolo and campo[2]==simbolo:
        return 1
    if campo[3]==simbolo and campo[4]==simbolo and campo[5]==simbolo:
        return 1
    if campo[6]==simbolo and campo[7]==simbolo and campo[8]==simbolo:
        return 1
    if campo[0]==simbolo and campo[1]==simbolo and campo[2]==simbolo:
        return 1
    if campo[0]==simbolo and campo[1]==simbolo and campo[2]==simbolo:
        return 1
    if campo[0]==simbolo and campo[1]==simbolo and campo[2]==simbolo:
        return 1
    if campo[0]==simbolo and campo[1]==simbolo and campo[2]==simbolo:
        return 1
    if campo[0]==simbolo and campo[1]==simbolo and campo[2]==simbolo:
        return 1
    
    
    
    
    
    