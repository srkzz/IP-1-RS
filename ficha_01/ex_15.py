num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

order = input("Digite 'c' para crescente ou 'd' para decrescente: ").lower()    

if order == 'c':
    sorted_numbers = sorted([num1, num2, num3])
    print("Os números em ordem crescente são:", sorted_numbers)
elif order == 'd':
    sorted_numbers = sorted([num1, num2, num3], reverse=True)
    print("Os números em ordem decrescente são:", sorted_numbers)
else:
    print("Opção inválida. Por favor, escolha 'c' ou 'd'.") 
