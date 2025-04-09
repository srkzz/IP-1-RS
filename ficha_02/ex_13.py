n = int(input("Quantos números deseja introduzir: "))
numbers = []

def order(numbers):
    for i in range(n):
        listaNumeros = input(f"Número {i+1}: ")
        numbers.append(int(listaNumeros))  # Converter o input para inteiros para facilitar a contagem.

    print("Lista de numeros inseridos:", numbers)
    
    # Verificar se está em ordem crescente
    if numbers == sorted(numbers, reverse=False):
        return 'Os numeros estão ordenados de forma crescente'
    # Verificar se está em ordem decrescente
    elif numbers == sorted(numbers, reverse=True):
        return 'Os numeros estão ordenados de forma decrescente'
    else:
        return 'Os numeros não estão ordenados de forma alguma.'

# Chamar a função e imprimir o resultado
resultado = order(numbers)
print(resultado)



