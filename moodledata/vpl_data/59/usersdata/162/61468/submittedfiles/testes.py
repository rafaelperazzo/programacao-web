def quantidade(a,b):
    cont=0
    for i in range(0,len(a),1):
        if a[i] is b:
            cont=cont+1
    return (cont)
n=int(input('n: '))
a=[]
for i in range(1,n+1,1):
    x=int(input('Digite n: '))
    a.append(x)
m=int(input('m: '))
b=[]
for i in range(1,m+1,1):
    y=int(input('m: '))
    b.append(y)
print(quantidade(a,b))