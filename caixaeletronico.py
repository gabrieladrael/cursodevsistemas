saldo = 1000

opcao = int(input("informe a opcao desejada: "))
if opcao == 1:
    saque = float(input("Informe o valor do saque: "))
    while saque > saldo:
        print("Opção inválida")
        saque = float(input("Informe o valor do saque: "))
    saldo -= saque
    print(f"Seu saldo é: {saldo}")  
elif opcao == 2:
    deposito = float(input("informe o valor do deposito: "))
    saldo += deposito
    print(f"Seu saldo é: {saldo}")    
elif opcao == 3:
    print(f"Seu saldo é: {saldo}")  
else:
    print("Opção inválida.")
    
  