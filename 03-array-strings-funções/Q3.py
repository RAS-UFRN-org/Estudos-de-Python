# 3. Reverter um array
# Dado um array, escreva um programa para reverter a ordem dos elementos.

quantidade = int(input("Quantidade de elementos: "))
arrayOri = []
arraySec = [0]*quantidade

for i in range(quantidade):
    numero = int(input("numero: "))
    arrayOri.append(numero)

for j in range(quantidade):
    arraySec[j] = arrayOri[len(arrayOri)-1-j]

print(arrayOri)
print(arraySec)