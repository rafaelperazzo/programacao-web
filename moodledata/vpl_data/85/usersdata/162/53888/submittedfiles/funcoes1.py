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
def consecutivo(k):
    cont=0
    for i in range(0,len(k),1):
        if i==0:
           if k[i]==k[i+1]:
           cont=cont+1
        elif i==len(k)-1:
            if k[i]=k[i-1]:
                cont=cont+1
        else:
            if k[i]==k[i+1] or k[i]=k[i-1]:
                cont=cont+1
    if cont!=0:
        return True
    else: 
        return False
        
n=int(input('Digite o tamanho da lista:'))
g=[]
c=[]
w=[]
for i in range(1,n+1,1):
    x=int(input('Digite os números:'))
    g.append(x)
            

