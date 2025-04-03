# Programa para encontrar o menor de três números inteiros

# Solicitar entrada de dados do usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

# Determinar o menor número
menor = min(num1, num2, num3)

# Exibir o menor número
print(f"O menor número é: {menor}")