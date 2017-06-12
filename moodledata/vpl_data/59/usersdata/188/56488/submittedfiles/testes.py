def matriz(a):
i=float(input('Digite o número de linhas:'))
j=float(input('Digite o número de colunas:'))
a=[]
a=np.zeros( (i,j) )
for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('Digite o elemento:'))

