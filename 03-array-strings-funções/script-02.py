max = 0
min = 10000000000000000000000

c = int(input("Digite um número: "))
max = c
min = c

while True:
    c = input("Digite um número: ")
    if c == "":
        break
    c = int(c)
    if c > max :
        max = c 
    
    if c < min :
        min = c

print(f"Min: {min}\nMax: {max}")
