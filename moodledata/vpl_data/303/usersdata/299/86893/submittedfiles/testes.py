def primo(n):
    cont=0
    for i in range(2,n,1):
        if n%i==0:
            cont=cont+1
            break
    if cont>0:
        return False
    else:
        return True
n=int(input(''))
print(primo(n))
while primo(n)==True:
    n=int(input(''))
    print(primo(n))
while primo(n)==False:
    n=int(input(''))
    print(primo(n))
    