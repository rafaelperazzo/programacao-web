def simpar(a):
    s=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            s=s+a[i]
    return(s)
def spar(a):
    s=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            s=s+a[i]
    return(s)
def qip(a):
    c=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            c=c+1
    return(c)
def qpar(a):
    c=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            c=c+1
    return(c)
n=int(input('Digite o tamanho da Lista:'))
b=[]
for i in range(1,n+1,1):
    v.append(int(input('Digite o elemento:'))
print(simpar(b))