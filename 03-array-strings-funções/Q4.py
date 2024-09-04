# 4. Contar ocorrências de um elemento
# Escreva um programa que recebe um array e conta quantas vezes um elemento específico aparece.

quantidade = int(input("Digite a quantidade de elementos: "))
num = int(input("Diga o numero para a contagem: "))
quantNum = 0
array = []

for i in range(quantidade):
    numeros = int(input("Digite o numero: "))
    array.append(numeros)

for j in range(quantidade):
    if array[j] == num:
        quantNum+=1

print(f'O numero {num} aparece {quantNum} vezes em seu array')