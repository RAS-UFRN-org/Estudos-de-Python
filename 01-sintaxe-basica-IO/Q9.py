# 9. *Calculando o Fatorial*  
# Escreva um programa que solicita ao usuário um número inteiro positivo e calcula o fatorial desse número usando um laço while ou for.

num = int(input("Digite o numero a fatorar: "))
fatorial = 1
i = 1
while i <= num:
    fatorial *= i
    i+=1

print(fatorial)