imposto1= 0.2
imposto2= 0.3
imposto3= 0.35
imposto4= 0.4
salario= int(input("Digite o seu salário: "))


if salario <= 15000:
    taxa = salario * imposto1

    print(f"Seu salário é: {salario} e o imposto a ser pago é: {taxa}")
    
elif salario >= 15000 and salario <= 20000:

    taxa = salario * imposto2
    
    print(f"Seu salário é: {salario} e o imposto a ser pago é: {taxa}")

elif salario >= 20000 and salario <= 25000:
    
    taxa = salario * imposto3
    
    print(f"Seu salário é: {salario} e o imposto a ser pago é: {taxa}")

else:
    
    taxa = salario * imposto4
    
    print(f"Seu salário é: {salario} e o imposto a ser pago é: {taxa}")