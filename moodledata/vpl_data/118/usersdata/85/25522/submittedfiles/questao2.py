

def tom(a):
    lf=[]
    for i in range(0,len(a),1):
        cont1=0
        if i==0:
            for l in range(0,len(a),1):
                if a[l]!=0:
                    cont1=cont1+1
                else:
                    break
            lf.append(cont1)
        cont2=0
        if i==len(a)-1:
            for j in range(len(a)-1,-1,-1):
                if a[j]!=0:
                    cont2=cont2+1
                else:
                    break
            lf.append(cont2)
        conte=0
        contd=0
        if i>0 and i<len(a)-1:
            for k in range(i,len(a),1):
                if a[k]!=0:
                    contd=contd+1
                else:
                    break
            for v in range(i,-1,-1):
                if a[v]!=0:
                    conte=conte+1
                else:
                    break
            if conte<=contd:
                lf.append(conte)
            elif contd<conte:
                lf.append(contd)
    return lf
    
n= int(input('Digite o valor de n: '))
a=[]

for i in range(0,n,1):
    a.append(input('Digite o elemento de a: '))
    
print tom(a)