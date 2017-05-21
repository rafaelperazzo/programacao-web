n=int(input('digite n: '))
for i in range(3,n+1,1):
    if i%2!=0 and i%3!=0 and i%5!=0:
        print(i)