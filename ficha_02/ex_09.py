

nr = int(input("Escreve um número: "))

while nr != 2:
    nr -= 1  
    i = nr 
    if i % 2 == 0:
        print(f"\t\t{i}")
else:
    print("Número 2 encontrado, saindo do loop.")
  
      