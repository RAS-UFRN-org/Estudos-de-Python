palavra = str(input("Digite a palavra: "))

for i in palavra:
    ultima = palavra[-i]
    if i == ultima:
        print("igual")
    else:
        print("diferente")
