
def SomaDigitos(n):
    soma=0
    while(n>0):
        resto%10
        soma=soma+resto
        n=(n**2)//10
    return(soma)
a=int(input('Digite um numero:'))
if SomaDigitos==1:
    print(É um número feliz')
else: 
    print('É um número infeliz')