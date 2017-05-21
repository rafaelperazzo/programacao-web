n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
multiplo=1
cont=0
while cont<=n:
    if multiplo%a==0 or multiplo%b==0:
        print(multiplo)
        cont=cont+1
    multiplo=multiplo+1