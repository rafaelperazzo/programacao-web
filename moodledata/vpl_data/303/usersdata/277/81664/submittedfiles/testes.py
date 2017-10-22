#x = 25
#x **= 1/2.0
#print(x)

# ENTRADA
n = int(input(' Digite o valor de n: '))
# PROCESSAMENTO
i = 2 			# Primeiro divisor a ser testado
contador = 0 		# Contador de divisores
while (i < (n-1)) :
    if n%i == 0 : 		# i eh divisor de n ?
        contador = contador + 1
    i += 1 		# Atualizar divisor a ser testado
# SAIDA
if contador > 0 :
    print('%d NAO EH primo!' % n)
else:
    print('%d EH primo!' % n)