palavra = input()
palindromo = True
i = 0
j = len(palavra) - 1
while i != j:
    if palavra[i] != palavra[j]:
        palindromo = False
        break
    i += 1
    j -= 1
print(palindromo)