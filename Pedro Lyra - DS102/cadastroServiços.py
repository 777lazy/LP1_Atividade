from datetime import datetime
def verificarVazio(resposta):
    if resposta == "":
        resposta = input("\nO campo não pode estar vazio. Tente novamente: ")
        return resposta
    else:
        return resposta

def exibirTodos(clientes):
    if len(clientes) >= 0:
        for cliente in clientes:
            print("\n"+"-"*50+"\n")
            print(f"Cliente: {cliente['cliente']}")
            print(f"Contato: {cliente['contato']}")
            print(f"Seviço: {cliente['servico']}")
            print(f"Data de Entrega: {cliente['dataEntrega']}")
            print("\n"+"-"*50+"\n")
    else:
        print("Você ainda não tem clientes.")

def exibirCliente(clientes, posicao):
    if posicao >= 0 and posicao < len(clientes):
        cliente = clientes[posicao]
        print("-"*50+"\n")
        print(f"Cliente: {cliente['cliente']}")
        print(f"Contato: {cliente['contato']}")
        print(f"Seviço: {cliente['servico']}")
        print(f"Data de Entrega: {cliente['dataEntrega']}")
        print("\n"+"-"*50)
    else:
        print('Cliente inexistente.')

def adcServico(cliente, contato, servico, dataEntrega):
    cadastro = {'cliente': cliente,'contato': contato,'servico': servico,'dataEntrega': dataEntrega}
    return cadastroServicos.append(cadastro)

def editarServico(clientes, posicao):
    if posicao >= 0 and posicao <= len(clientes):
        cliente = clientes[posicao]
        opcaoEditar = int(input("Escolha o que quer editar:\n1 - Cliente.\n2 - Contato.\n3 - Serviço.\n4 - Data de Entrega.\n5 - Tudo."))
        match opcaoEditar:
            case 1:
                cliente['cliente'] = verificarVazio(input("Cliente: "))
            case 2:
                cliente['contato'] = verificarVazio(input("Contato: "))
            case 3:
                cliente['servico'] = verificarVazio(input("Serviço: "))
            case 4:
                stringEntrega = verificarVazio(input("Data de Entrega (dd/mm/aaaa): "))
                cliente['dataEntrega'] = datetime.strptime(stringEntrega, "%d/%m/%Y")
            case 5:
                cliente['cliente'] = verificarVazio(input("Cliente: "))
                cliente['contato'] = verificarVazio(input("Contato: "))
                cliente['servico'] = verificarVazio(input("Serviço: "))
                stringEntrega = verificarVazio(input("Data de Entrega (dd/mm/aaaa): "))
                cliente['dataEntrega'] = datetime.strptime(stringEntrega, "%d/%m/%Y")

cadastroServicos = [
                    {'cliente': 'Ygor Canalli',
                     'contato': 'ygorcanalli@cp2.g12,br',
                     'servico': 'Dever de LP1',
                     'dataEntrega': '26/02/2025'}
                    ]

print("Seja bem-vindo(a) ao programa SeuSERVIÇO")
while True:
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
                varCliente = verificarVazio(input("Cliente: "))
                varContato = verificarVazio(input("Contato: "))
                varServiço = verificarVazio(input("Serviço: "))
                stringData = verificarVazio(input("Data de Entrega (dd/mm/aaaa): "))
                varData = datetime.strptime(stringData, "%d/%m/%Y")
            
                adcServico(varCliente, varContato, varServiço, varData.strftime('%d/%m/%Y'))
                print("Cliente adicionado com sucesso!")
                input()

            case 3:
                print("\nVocê escolheu remover.")
                cadastroServicos.pop(int(input("\nEscolha o Serviço: ")))
                input()
            case 4:
                print("\nVocê escolheu editar.")
                editarServico(cadastroServicos, int(input("\nEscolha o serviço: ")))
                input()
    else:
        print('Opção não encontrada. Tente novamente: ')
        pass