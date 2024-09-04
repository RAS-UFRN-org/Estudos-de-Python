contador = 0
for i in range(3):  # um for de 3 elementos
    numero = int(input(f"Digite o número {i+1}: "))
    contador = numero + contador

media = contador / 3

print(media)
