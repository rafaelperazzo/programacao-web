# -*- coding: utf-8 -*-
p=int(input("Digite p: "))
while(True):
    if p<0:
        p=int(input("Digite p: "))
    else:
        break
q=int(input("Digite q: "))
while(True):
    if q<0:
        q=int(input("Digite q: "))
    else:
        break
if str(p) in str(q):
    print("S")
else:
    print("N")
    
