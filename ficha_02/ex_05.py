
nr = int(input("Escreve um número de inicio: "))
nr2 = int(input("Escreve um número de fim: "))

for i in range(nr-1, nr2):
        print("Número", i+1)
        if i == nr2:
            break