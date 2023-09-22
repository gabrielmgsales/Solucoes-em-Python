menu = """

[1]Depositar
[2]Sacar
[3]Extrato
[4]Saldo
[5]Sair

=> """

saldo = 0 # Antes de sacar é necessário fazer um depósito, opção 1 do menu
limite = 1000 # Limite de valor de saque
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    Opcao = input (menu)

    if Opcao == '1':
        self_valor = input('Digite o valor para depósito: R$').replace(',', '.')        
        valor = float(self_valor)

        if valor > 0:

            print('\nDepósito feito com sucesso')
            saldo += valor
            extrato += f'Depósito: Valor R${valor:.2f}\n'

        else:
            print('Valor informado para depósito é inválido')

    elif Opcao == '2':

        self_valor = input('Digite o valor para sacar: R$').replace(',', '.')
        valor = float(self_valor)
        print('\nSaque realizado com sucesso')

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print('Você não possui saldo suficiente')
        
        elif excedeu_limite:
            print('O valor do saque excede o valor permitido por dia')

        elif excedeu_saques:
            print('Você excedeu o número de saques permitidos por dia')

        elif valor > 0:
            saldo -= valor
            extrato = f'saque: R${valor :.2f}\n'
            numero_saques += 1

        else:
            print('O valor informado é inválido')

    elif Opcao == '3':
        print('----------EXTRATO----------\n')

        print('Não foram realizadas movimentações'if not extrato else extrato)
        print(f'saldo: R${saldo:.2f}\n')

        print('----------------------------')

    elif Opcao == '4':
        print(f'Saldo disponível para saque: R${saldo:.2f}')
    
    elif Opcao == '5':
        print('Obrigado por utilizar nossos serviços')
        break

    else:
        print('Opção inválida')        