def épar(x):
    return(x%2==0)
def par_ou_impar(x):
    if épar(x):
        return 'par'
    else:
        return 'impar'
n=(int(input('n'))
print(par_ou_impar(4))
print(par_ou_impar(5))
        