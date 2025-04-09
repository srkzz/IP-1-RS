def main():
    total_seconds = 0

    for i in range(1, 6):
        print(f"Informe a duração da música {i}:")
        minutos = int(input("Minutos: "))
        segundos = int(input("Segundos: "))
        total_seconds += minutos * 60 + segundos

    horas = total_seconds // 3600
    minutos = (total_seconds % 3600) // 60
    segundos = total_seconds % 60

    print(f"A duração total do álbum é: {horas:02}:{minutos:02}:{segundos:02}")

if __name__ == "__main__":
    main()