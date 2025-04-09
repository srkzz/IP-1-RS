limite = int(input("Escreve um número limite: "))
salto = int(input("Escreve um número para salto: "))



if salto and limite > 0:
    i = 0
    while i < limite:
        print(f"\t{i}")
        i += salto