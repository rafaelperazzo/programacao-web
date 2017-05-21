n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
multiplo=1
cont=0
for cont in range(1,n+1,1):
    if multiplo%a==0 or multiplo%b==0:
        print(multiplo)
    multiplo=multiplo+1