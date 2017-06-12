
def feliz(n):
    if n==1:
        return(True)
    elif n==4:
        return(False)
    else:
        soma=0
        lista=[]
        while n!=0:
            lista.append(0,n%10)
            n=n/10
            soma=soma+(lista**2)
        return(soma)

n=int(input('Digite o número:'))
if feliz(n):
    print('É feliz')
else:
    print('Não é feliz:')
            