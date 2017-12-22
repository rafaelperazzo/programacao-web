def converterBinario(valor):
    resultado=''
    while valor>1:
        if valor%2==0:
            resultado += '1'
        else:
            resultado += '0'
        valor = valor/2
    return resultado[::-1]
a = 4
print(converterBinario(a))