nr1 = int(input("Escreve um número: "))
nr2 = int(input("Escreve um número: "))


for i in range(nr1, nr2):
    if i % 5 == 0:
        print(f"\t{i}")
    else:
        continue
