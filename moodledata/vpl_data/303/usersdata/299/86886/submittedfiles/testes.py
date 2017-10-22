cont=0
def primo(n):
    for i in range(2,n,1):
        if n%i==0:
            cont=cont+1
            break
    if cont>0:
        return True
    else:
        return False