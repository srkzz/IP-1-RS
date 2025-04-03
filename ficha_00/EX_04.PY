import math

# Solicita o raio da circunferência ao usuário
raio = float(input(" Digite o raio: ")) 

# Calcula a área da circunferência
area = math.pi * (raio ** 2)

# Exibe o resultado
print(f"A área da circunferência é: {area:.3f}")