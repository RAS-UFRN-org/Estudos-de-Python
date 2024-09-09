# 6. Encontrar a diferença entre dois arrays
# Dado dois arrays, retorne os elementos que estão presentes no primeiro array, mas não no segundo.

array1 = []
array2 = []
quantArray1 = int(input("Digite a quantidade do primeiro array: "))
quantArray2 = int(input("Digite a quantidade do segundo array: "))

for i in range(quantArray1):
    num1 = int(input("Digite o numero: "))
    array1.append(num1)

print("Agora digite os numeros do segundo array")

for j in range(quantArray2):
    num2 = int(input("Digite o numero: "))
    array2.append(num2)

notInArray2 = []
for numero in array1:
    if numero not in array2:
        notInArray2.append(numero)

print(notInArray2)