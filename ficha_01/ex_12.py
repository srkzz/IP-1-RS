def menu():
    while True:
        print("\nMenu:")
        print("1. Criar")
        print("2. Atualizar")
        print("3. Eliminar")
        print("4. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                print("Opção 'Criar' selecionada.")
                #  lógica para criar aqui
            elif opcao == 2:
                print("Opção 'Atualizar' selecionada.")
                # lógica para atualizar aqui
            elif opcao == 3:
                print("Opção 'Eliminar' selecionada.")
                #  lógica para eliminar aqui
            elif opcao == 4:
                print("Saindo do programa...")
                break
            else:
                print("Erro: Opção inválida. Tente novamente.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
    menu()