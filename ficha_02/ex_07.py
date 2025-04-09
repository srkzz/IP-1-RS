nr = int(input("Escreve um número: "))

for i in range(nr-6, nr+5):
        i += 1
        print(f"Número {i}") 
    
        if i == nr+6:
            break  

