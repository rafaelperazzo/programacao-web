
n=int(input('linhas & colunas:'))
a=np.zeros((n,n))

for i in range (0,a.shape[0],1):
    for l in range(0,a.shape[1],1):
        a[a,l]=float(input('valor:'))