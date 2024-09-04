# 2. Maior e menor número de um array
# Crie um programa que recebe um array e encontra o maior e o menor número presente nele.

quantidade = int(input("Digite a quantidade de elementos do seu array: "))
array = []

for i in range(quantidade):
    numero =  int(input("Diga o numero: "))
    array.append(numero)

maior = array[0]
menor = array[0]

for j in range(len(array)):
    if array[j]>maior:
        maior = array[j]
    if array[j]<menor:
        menor = array[j]

print(f'O maior elemento da lista é {maior} e o menor é {menor}')