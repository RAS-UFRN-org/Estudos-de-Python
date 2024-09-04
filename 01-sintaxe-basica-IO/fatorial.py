# escreva um programa que calcula o fatorial do numero digitado

numero = int(input("Digite o numero: "))
somador = 1
# range(start, stop, step)
for i in range(0, numero):
    somador = (somador + (i+1))
    print(somador)
