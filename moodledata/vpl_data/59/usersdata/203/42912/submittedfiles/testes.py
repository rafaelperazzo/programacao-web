n=int(input('digite n: '))
cont60=0
cont59=0
for n in range(1,n+1,1):
    idade=int(input('digite idade: '))
    if idade>60:
        cont60=cont60+1
    else:
        cont59=cont59+1
print(cont60)
print(cont59)