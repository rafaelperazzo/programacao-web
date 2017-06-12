
def feliz(n):
    if n==1:
        return(True)
    elif n==4:
        return(False)
    else:
        soma=0
        lista=[]
        while n!=0:
            resto=n%10
            lista.append(resto)
            n=n/10
            soma=soma+(lista**2)
        return(soma)

n=int(input('Digite o número:'))
if feliz(n):
    print('É feliz')
else:
    print('Não é feliz:')
            