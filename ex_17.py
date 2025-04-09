salario= int(input("Digite o seu salário: "))
credito = salario

if salario <= 2000: 

    print(f"Seu salário é: R${salario} logo não tem direito a crédito")
    
elif salario >= 2000 and salario <= 4000:
    
    print(f"Seu salário é: R${salario} logo tem direito a 20% de crédito que será {credito*0.2}")

elif salario >= 4000 and salario <= 6000:
    
    print(f"Seu salário é: R${salario} logo tem direito a 30% de crédito que será {credito*0.3}")

elif salario >= 6000:

    print(f"Seu salário é: R${salario} logo tem direito a 40% de crédito que será {credito*0.4}")

else:
    
    print("Não seja pobre")