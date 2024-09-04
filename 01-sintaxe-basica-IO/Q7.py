# 7. *Calculando a Área de um Círculo*  
# Escreva um programa que solicita ao usuário o raio de um círculo e calcula a área. (Dica: Área = π*r², onde π = 3.14159)

import math 

num_raio = float(input("Digite o numero do raio: "))
area = math.pi*(num_raio**2)

print(f'A area do circulo é: {round(area, 3)}')