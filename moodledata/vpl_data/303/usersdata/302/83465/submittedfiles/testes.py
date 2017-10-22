while(true):
    while(true):
        n = int(input('Digite um numero positivo'))
        if n >=0:
            break
f = 1
for i in range(2,n+1,1):
    f = f*1
print('%d=%d' %(n,f))
opt = input('deseja continuar? [S ou N]')
if opt == 'N':
    print('\n\nATE BREVE!')
    break
       