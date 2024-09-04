lista1 = [2,3,4,6,7,8,9,-10,2]
lista_de_somas = []
soma_total = -100000000

for i in range(len(lista1)):
    for j in range(i, len(lista1)):
        soma_atual = sum(lista1[i:j+1])
        lista_de_somas.append(soma_atual)
        if soma_atual > soma_total:
            soma_total = soma_atual
            
print(soma_total)
