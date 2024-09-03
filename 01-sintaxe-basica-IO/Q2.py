# 2. *Entrada e Saída Simples*  
# Escreva um programa que solicita ao usuário seu nome e idade, e depois imprime uma mensagem dizendo "Olá, [nome]! Você tem [idade] anos.

nome = input("Digite seu nome: ")
idade = input("Diga sua idade: ")
idade_int = int(idade)

print(f"Olá, {nome}! Você tem {idade_int} anos")