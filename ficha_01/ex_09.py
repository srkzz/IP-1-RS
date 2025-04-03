# Programa para realizar operações aritméticas

# Pedir entrada de dois números reais ao utilizador
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Pedir ao utilizador a operação aritmética
operacao = input("Digite a operação aritmética (+, -, *, /): ")

# Realizar a operação e apresentar o resultado
if operacao == '+':
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Erro: Operação inválida.")