n=int(input('valor:'))
i=1
while i*(i+1)*(i+2)<n:
    i=i+1
if i==n:
    print ('sim')
else:
    print ('não')