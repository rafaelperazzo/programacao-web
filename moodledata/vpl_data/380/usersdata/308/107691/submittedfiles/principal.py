def converterDecimal(valor):
    resultado = 0
    expoente = len(valor)
    for i in range (len(valor)-1, -1, -1):
        print(valor[i])
        resultado += int(valor[i])*(2**(i))
        expoente -= 1 
    return resultado

print(converterDecimal('1011'))

