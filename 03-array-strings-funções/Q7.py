# 7. Mover todos os zeros para o final
# Escreva um programa que, dado um array de números inteiros, mova todos os zeros para o final, mantendo a ordem dos outros elementos.

arrayOriginal = []
quantArray = int(input("Digite a quantidade do array: "))

for i in range(quantArray):
    num = int(input("Digite o numero: "))
    arrayOriginal.append(num)

arrayOrganizado = []
zeros = []
for num in arrayOriginal:
    if num == 0:
        zeros.append(num)
    else:
        arrayOrganizado.append(num)
        
arrayOrganizado.extend(zeros)
print(arrayOrganizado)