# 5. Remover duplicatas de um array
# Escreva um programa que recebe um array e retorna um novo array sem elementos duplicados.

quantidade = int(input("Digite o numero de elementos q deseja: "))
arrayOri = []

for i in range(quantidade):
    numeros = int(input("Digite o numero: "))
    arrayOri.append(numeros)

duplicado = 0
for j in range(quantidade):
    for i in range(quantidade):
        if arrayOri[i]==arrayOri[j]:
            duplicado = arrayOri[i]

arrayOri.remove(duplicado)
print(arrayOri)