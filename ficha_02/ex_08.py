nr = int(input("Escreve um número: "))


while nr != -1:
    print("Número", nr)
    nr = int(input("Escreve um número: "))
    if nr == -1:
        print("Número de fecho. Encerrando o programa.")
        exit()