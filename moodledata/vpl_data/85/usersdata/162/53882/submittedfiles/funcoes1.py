def crescente(k):
    cont=0
    for i in range(o,len(k),1):
        if k[i]>k[i-1]:
            cont=cont+1
        if cont==len(k)-1:    
            return True
        else:
            return False
def decrescente(k):
    cont=0
    for i in range(0,len(k),1):
        if k[i]<k[i-1]:
            cont=cont+1
        if cont==len(k)-1:
            return True
        else:
            return False
            

