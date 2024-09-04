# 8. *Conversor de Temperatura*  
# Escreva um programa que solicita ao usuário uma temperatura em graus Celsius e converte para Fahrenheit. (Dica: F = (C \* 9/5) + 32)

num_C = float(input("Digite a temperatura: "))
num_F = (num_C * (9/5)) + 32

print(f'A temperatura: {num_C} graus celsius em Fahrenheit é: {num_F}')