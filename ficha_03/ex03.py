nr1 = 0
contador = 0
nr2 = 0


nr1 = int(input("Escolha um número secreto: "))
while nr1 != nr2:
    nr2 = int(input("Escolha um número para tentar adivinhar: "))
    if nr1 > nr2:
        print ("Estava quase.")
        print("O NR secreto é maior")  
    elif nr2 > nr1:
        print ("Estava quase.")
        print("O NR secreto é menor")
    else:
        print(f"Parabéns acertou, demorou {contador} tentativas.")
    contador += 1 


