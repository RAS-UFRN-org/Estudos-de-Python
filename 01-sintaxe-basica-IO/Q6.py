# 6. *Verificando Par ou Ímpar*  
# Escreva um programa que solicita ao usuário um número inteiro e imprime se o número é par ou ímpar.

num = float(input("Digite um numero: "))

if num%2==0:
    print(f"O numero {num} é par")
else:
    print(f'O numero {num} é impar')