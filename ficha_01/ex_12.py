# Solicita ao usuário que insira um horário no formato de 24 horas
horario_24h = input("Digite um horário no formato 24 horas (HH:MM): ")

# Divide o horário em horas e minutos
horas, minutos = map(int, horario_24h.split(':'))

# Determina se é AM ou PM
if horas >= 12:
    periodo = "PM"
else:
    periodo = "AM"

# Converte as horas para o formato de 12 horas
horas_12h = horas % 12
if horas_12h == 0:
    horas_12h = 12

# Exibe o horário no formato de 12 horas
print(f"{horas_12h}:{minutos:02d} {periodo}")