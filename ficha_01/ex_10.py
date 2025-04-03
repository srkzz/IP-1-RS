# Programa bancário para simular operações de crédito ou débito

# Solicitar o saldo inicial do usuário
saldo = float(input("Digite o saldo inicial da conta: "))

# Solicitar o tipo de operação
operacao = input("Digite o tipo de operação (crédito ou débito): ").strip().lower()

# Solicitar o valor da operação
valor = float(input("Digite o valor da operação: "))

# Processar a operação
if operacao == "crédito":
    saldo += valor
elif operacao == "débito":
    saldo -= valor
else:
    print("Operação inválida. Por favor, escolha 'crédito' ou 'débito'.")

# Exibir o saldo final
print(f"Saldo final: R$ {saldo:.2f}")

# Verificar se o saldo final é positivo ou negativo
if saldo >= 0:
    print("O saldo final é positivo.")
else:
    print("O saldo final é negativo.")