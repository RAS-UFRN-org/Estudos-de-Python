def fatorial(n):
    if n == 0:
        return 1

    return n * fatorial(n - 1)

num = int(input("Digite um número: "))

fat = fatorial(num)

print(f"Seu fatorial é {fat}")
