n=int(input('digite n: '))
termos=0
teste=n
soma=0
i=0
while teste>0:
    teste=teste//10
    termos=termos+1
while n<0:
    resto=n%10
    soma=soma+resto*(2**i)
    n=n//10
    i=i+1
    