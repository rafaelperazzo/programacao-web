def primo(n):
    cont=0
    for i in range(2,n,1):
        if n%i==0:
            cont=cont+1
    if cont==0:
        return true
    else:
        return false
n1=int(input('n1'))
n2=int(input('n2'))
if primo(n1):
    print('%primo' %n1)
else:
    print('%n[ao primo' %n1)
if primo(n2):
    print('%primo' %n2)
else:
    print('%n[ao primo' %n2)    
    