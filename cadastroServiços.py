from datetime import datetime
import json

def lerJSON():
    with open("cadastroServicos.json", "r") as meuArquivo:
        cadastroServicos = json.load(meuArquivo)
        return cadastroServicos
    
def salvarJSON(lista):
    with open("cadastroServicos.json", "w") as meuArquivo:
        meuArquivo.write(lista)
        
def verificarVazio(resposta):
    if resposta == "":
        resposta = input("\nO campo não pode estar vazio. Tente novamente: ")
        return resposta
    else:
        return resposta
    
def verificarData(resposta):
        try:
            dataEntrega = datetime.strptime(resposta, "%d/%m/%Y")
            while True:
                if dataEntrega < datetime.now():
                    print('Data inválida. Não pode ser uma data passada.\nTente novamente.')
                    dataEntrega = input(": ")
                else:
                    return dataEntrega
        except ValueError:
            print('Data inválida. Use o formato dd/mm/aaaa.')
            dataEntrega = input(": ")

def exibirTodos(clientes):
    if len(clientes) >= 0:
        y = 0
        for cliente in clientes:
            y += 1
            print("\n"+"-"*10+f" Dados do Serviço {y} "+"-"*10+"\n")
            print(f"Cliente: {cliente['cliente']}")
            print(f"Contato: {cliente['contato']}")
            print(f"Seviço: {cliente['servico']}")
            print(f"Data de Entrega: {cliente['dataEntrega']}")
            print("\n"+"-"*37+"\n")
    else:
        print("Você ainda não tem clientes.")

def exibirCliente(clientes, posicao):
    posicao -= 1
    if posicao >= 0 and posicao < len(clientes):
        cliente = clientes[posicao]
        print(f"\nServiço {posicao+1}")
        print("\n"+"-"*10+f" Dados do Serviço {posicao+1} "+"-"*10+"\n")
        print(f"Cliente: {cliente['cliente']}")
        print(f"Contato: {cliente['contato']}")
        print(f"Seviço: {cliente['servico']}")
        print(f"Data de Entrega: {cliente['dataEntrega']}")
        print("\n"+"-"*37+"\n")
    else:
        print('Cliente inexistente.')

def adcServico(cliente, contato, servico, dataEntrega):
    cadastro = {'cliente': cliente,'contato': contato,'servico': servico,'dataEntrega': dataEntrega}
    return cadastroServicos.append(cadastro)

def removerServico(clientes, posicao):
    while True:
        posicao -= 1
        if posicao >= 0 and posicao <= len(clientes):
            cadastroServicos.pop(posicao)
            break
        else:
            print("Cliente inexistente.")
            posicao = input("Tente novamente: ")

def editarServico(clientes, posicao):
    while True:
        posicao -= 1
        if posicao >= 0 and posicao <= len(clientes):
            cliente = clientes[posicao]
            opcaoEditar = int(input("Escolha o que quer editar:\n1 - Cliente.\n2 - Contato.\n3 - Serviço.\n4 - Data de Entrega.\n5 - Tudo.\n\n"))
            match opcaoEditar:
                case 1:
                    cliente['cliente'] = verificarVazio(input("Editar Cliente: "))
                    break
                case 2:
                    cliente['contato'] = verificarVazio(input("Editar Contato: "))
                    break
                case 3:
                    cliente['servico'] = verificarVazio(input("Editar Serviço: "))
                    break
                case 4:
                    stringEntrega = verificarData(input("Data de Entrega (dd/mm/aaaa): "))
                    cliente['dataEntrega'] = datetime.strptime(stringEntrega, "%d/%m/%Y")
                    break
                case 5:
                    cliente['cliente'] = verificarVazio(input("Editar Cliente: "))
                    cliente['contato'] = verificarVazio(input("Editar Contato: "))
                    cliente['servico'] = verificarVazio(input("Editar Serviço: "))
                    stringEntrega = verificarData(input("Editar Data de Entrega (dd/mm/aaaa): "))
                    cliente['dataEntrega'] = datetime.strptime(stringEntrega, "%d/%m/%Y")
                    break
        else:
            print("Cliente inexistente.")
            posicao = input("Tente novamente: ")

maximoCadastros = 5
cadastroServicos = []
salvarJSON(json.dumps(cadastroServicos, indent=4))
cadastroServicos = lerJSON()
print("\nSeja bem-vindo(a) ao programa SeuSERVIÇO")
while True:
    
    salvarJSON(json.dumps(cadastroServicos, indent=4))
    
    print("\n"+"-"*10+" Menu "+"-"*10+"\n")
    print("O que deseja fazer agora?\n\n1 - Exibir seus serviços.\n2 - Adicionar serviço.\n3 - Remover serviço.\n4 - Editar serviço.")
    
    opcao = int(input("Escolha uma opção: "))
    if opcao >= 1 and opcao <=4:
        match opcao:
            case 1:
                print("\nVocê escolheu exibir.")
                print('\n1 - Exibir todos.\n2 - Exibir um serviço.')
                repetir2 = True
                while repetir2:
                    opcaoExibir = int(input("\nEscolha uma opção: "))
                    if opcaoExibir >= 1 and opcaoExibir <= 2:
                        match opcaoExibir:
                            case 1:
                                exibirTodos(cadastroServicos)
                                repetir2 = False
                                input()
                            case 2:
                                exibirCliente(cadastroServicos, int(input("\nEscolha o serviço: ")))
                                repetir2 = False
                                input()
                    else:
                        print('Opção não encontrada. Tente novamente:')
            case 2:
                print("\nVocê escolheu adicionar.")
                if len(cadastroServicos) < maximoCadastros:
                    varCliente = verificarVazio(input("Cliente: "))
                    varContato = verificarVazio(input("Contato: "))
                    varServiço = verificarVazio(input("Serviço: "))
                    varData = verificarData(input("Data de Entrega (dd/mm/aaaa): "))
            
                    adcServico(varCliente, varContato, varServiço, varData.strftime('%d/%m/%Y'))
                    print("ADICIONADO com sucesso!")
                    input()
                else:
                    print("Limite máximo de clientes atingido, termine seus serviços!")

            case 3:
                print("\nVocê escolheu remover.")
                removerServico(cadastroServicos, int(input("\nEscolha o Serviço: ")))
                print("REMOVIDO com sucesso!")
                input()
            case 4:
                print("\nVocê escolheu editar.")
                editarServico(cadastroServicos, int(input("\nEscolha o serviço: ")))
                print("EDITADO com sucesso!")
                input()
    else:
        print('\nOpção não encontrada. Tente novamente: ')
        pass