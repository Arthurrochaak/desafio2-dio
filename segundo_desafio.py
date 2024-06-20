import textwrap


def menu():

    menu = """
    Bem vindo ao terminal de atendimento bancário.\n
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuario
    [5] Lista de contas por CPF
    [6] Cadastrar conta

    [0] Sair

    Informe o serviço: """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
         saldo += valor
         extrato += f"Depósito efetuado no valor de: R$ {valor:.2f}\n"
         print("Depósito realizado com sucesso!")
    else:
            print("O valor informado é inválido!")    
    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite_saque, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_saque
    excedeu_saques = numero_saques > limite_saques
        
    if excedeu_saldo:
        print ("Saldo insuficiente!")

    elif excedeu_limite:
        print ("Essa operação excedeu o limite de saque.")

    elif excedeu_saques:
         print("Você atingiu o número máximo de saques diários.")
    elif valor>0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print ("O valor informado é inválido!")

    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print ("\n EXTRATO: ")
    print ("Não foram realizadas movimentações." if not extrato else extrato)
    print (f"\nSaldo: R$ {saldo:.2f}\n")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente números): ")
    usuario = contas_usuario(cpf, usuarios)
    
    if usuario:
        print("\n O CPF informado já foi cadastrado em outro usuário!")
        return
    
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereço = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})

    print("Usuário cadastrado com sucesso!")

def contas_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = contas_usuario(cpf,usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))



def main():

    agencia = "0001"
    saldo = 0
    limite_saque = 500
    numero_saques = 0
    limite_saques = 3
    extrato = ""
    usuarios = []
    contas = []


    while True:
        escolha = menu()

        if escolha == "1":
            valor = float(input("Informe o valor do depósito: \n R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif escolha == "2":
            valor = float(input("Informe o valor do saque: \n R$ "))    
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_saque=limite_saque,
                numero_saques=numero_saques,
                limite_saques=limite_saques,
            )

        elif escolha == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif escolha == "4": #novo usuario
            criar_usuario(usuarios)

        elif escolha == "5": #lista de contas por cpf
            listar_contas(contas)

        elif escolha == "6": #cadastrar conta
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif escolha == "0":
            break

        else :
            print("Comando inválido.")


main()
