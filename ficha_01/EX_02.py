imposto1= 0.02
imposto2= 0.03

salario= int(input("Digite o seu salário: "))


if salario <= 15000:
    taxa = salario * imposto1

    print(f"Seu salário é: {salario} e o imposto a ser pago é: {taxa}")
    
else:

    taxa = salario * imposto2
    
    print(f"Seu salário é: {salario} e o imposto a ser pago é: {taxa}")