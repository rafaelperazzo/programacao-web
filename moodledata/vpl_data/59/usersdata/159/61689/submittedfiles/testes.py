# -*- coding: utf-8 -*-
def primo (n):
    j=1
    cont=0
    while cont<n:
        for i in range (2,j,1):
            if j%i==0:
                break
            else:
                for k in range (2,(j+2),1):
                    if (j+2)%k==0:
                        break
                    else:
                        cont=cont+1
        j=j+1
    return (j-1,j+1)
    
n=int(input('Digite n:'))
print(primo(n))