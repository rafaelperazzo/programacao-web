def épar(a):
    return(a%2==0)
def par_ou_impar(a):
    if épar(a):
        return('par')
    else:
        return('impar')
print(par_ou_impar(10))
print(par_ou_impar(11))