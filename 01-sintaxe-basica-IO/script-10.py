from collections import deque


palavra = input("Digite a palavra: ")

stack = deque()

for char in palavra:
    stack.append(char)


for char in palavra:
    if char != stack.pop():
        print("Não é palíndromo.")
        break
else:
    print("É palíndromo.")


