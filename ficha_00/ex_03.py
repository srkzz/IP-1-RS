# Programa para calcular a área e o perímetro de um retângulo

# Solicita ao usuário a largura e a altura do retângulo
largura = float(input("Informe a largura do retângulo: "))
altura = float(input("Informe a altura do retângulo: "))

# Calcula a área e o perímetro
area = largura * altura
perimetro = 2 * (largura + altura)

# Exibe os resultados
print(f"A área do retângulo é: {area}")
print(f"O perímetro do retângulo é: {perimetro}")