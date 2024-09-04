# 1. Soma dos elementos de um array
# Escreva um programa que receba um array de números e retorne a soma de todos os seus elementos.

lista_num = []
quantidade_de_num = int(input("Digite a quantidade de elementos: "))

for i in range(quantidade_de_num):
    numeros = int(input("Diga o numero: "))
    lista_num.append(numeros)

soma = sum(lista_num)

print(f'A soma dos seus valores é: {soma}')