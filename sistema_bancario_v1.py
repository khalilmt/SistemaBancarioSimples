# Variaveis

menu = """
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_N_SAQUES = 3

# Bloco de Execução

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do Depoisto: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou. Favor informar valor valido")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_N_SAQUES
        
        if excedeu_saldo:
            print("Saldo Insuficiente.")
        elif excedeu_limite:
            print("Valor do Saque Excede Limite")
        elif excedeu_saques:
            print("Numero de Saques Diarios Excedio")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "e":
        print("\n##########Extrato##########")
        print("Não foram realizados transações" if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("#############################")

    elif opcao == "q":
        break
    else:
        print("Opção Invalida")      