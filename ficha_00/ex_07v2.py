num1 = float(input(" Digite o preço do primeiro produto: "))
num2 = float(input(" Digite o preço do segundo produto: "))
num3 = float(input(" Digite o preço do terceiro produto: "))

totalPagar = num1 + num2 + num3
print(f" O total a pagar é: {totalPagar}")

desconto = totalPagar * 0.10 
totaldesconto = totalPagar - desconto
print(f" O desconto é: {desconto}")
print(f" O total com desconto é: {totaldesconto}")  

