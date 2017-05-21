n=int(input('digite n: '))
termos=0
teste=n
while teste>0:
    teste=teste//10
    termos=termos+1
print(termos)