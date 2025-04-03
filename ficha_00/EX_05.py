num1 = 0
num2 = 0 
num3 = 0

num1 = float(input(" Digite a nota 1: ")) 
num2 = float(input(" Digite a nota 2: ")) 
num3 = float(input(" Digite a nota 3: ")) 

media_aritmetica = (num1 + num2 + num3) / 3
print(f"A média aritmética é: {media_aritmetica}")


media_ponderada = (num1 * 0.20 + num2 * 0.30 + num3 * 0.50)
print(f"A média ponderada é: {media_ponderada}")

if media_ponderada >= 9.5:
    print("Aprovado")

else:
    print("Reprovado")
