def converterBinario(valor):
    resultado=''
    while valor>1:
        resultado += valor%2

        valor = valor/2
    return resultado[::-1]
a = 4
print(converterBinario(a))