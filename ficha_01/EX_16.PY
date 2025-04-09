# Solicita ao usuário um valor em euros (múltiplo de 5)
valor = int(input("Digite um valor em euros (múltiplo de 5): "))

# Verifica se o valor é múltiplo de 5
if valor % 5 != 0:
    print("O valor deve ser múltiplo de 5.")
else:
    # Lista de notas disponíveis
    notas = [200, 100, 50, 20, 10, 5]
    resultado = {}

    # Calcula a quantidade de cada nota necessária
    for nota in notas:
        quantidade = valor // nota
        if quantidade > 0:
            resultado[nota] = quantidade
        valor %= nota

    # Exibe o resultado
    print("Menor quantidade de notas necessárias:")
    for nota, quantidade in resultado.items():
        print(f"{quantidade} nota(s) de {nota}€")