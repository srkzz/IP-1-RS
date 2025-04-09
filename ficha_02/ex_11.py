
count_0_25 = 0
count_26_50 = 0
count_51_75 = 0
count_76_100 = 0

nr = int(input("Escreve um número: "))

while nr >= 0:
  
    if 0 <= nr <= 25:
        count_0_25 += 1
    elif 26 <= nr <= 50:
        count_26_50 += 1
    elif 51 <= nr <= 75:
        count_51_75 += 1
    elif 76 <= nr <= 100:
        count_76_100 += 1
    nr = int(input("Escreve um número: "))

print("\nNúmero negativo encontrado.")
print("\nResultados:")
print(f"Números no intervalo [0-25]: {count_0_25}")
print(f"Números no intervalo [26-50]: {count_26_50}")
print(f"Números no intervalo [51-75]: {count_51_75}")
print(f"Números no intervalo [76-100]: {count_76_100}")
