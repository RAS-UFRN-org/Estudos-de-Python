#4. *Calculadora de Média*  
#Escreva um programa que solicita ao usuário três notas, calcula a média aritmética e imprime o resultado.

numeros = []
for i in range(3):
    numero = int(input("Digite o numero: "))
    numeros.append(numero)

soma = sum(numeros)
media = soma/3

print(media)