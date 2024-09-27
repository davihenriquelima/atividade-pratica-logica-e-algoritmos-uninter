# variáveis globais
funcionarios = []
id_funcionario = 7400

# função de cadastro de funcionários
def cadastrar_funcionario(id):
    print('*'*100)
    print('-'*33,'Menu de cadastro de funcionários','-'* 33)
    print('Id do funcionário: {}' .format(id))
    nome = input('Entre com o nome do funcionário: ')
    setor = input('Entre com o setor do funcionário: ')
    salario = int(input('Entre com o salário do funcionário: '))
    # após recebermos esses dados, armazenamos em um dicionário. Objeto com chave e valor
    dicionario_funcionario = {'id': id, 'nome': nome, 'setor': setor, 'salario': salario}
    # adicionamos uma cópia do dicionario (objeto) na lista de funcionários
    funcionarios.append(dicionario_funcionario.copy())

# função de consulta de funcionários
def consultar_funcionario():
    print('*'*100)
    print('-'*33,'Menu de consulta de funcionários','-'* 33)
    while True:
        opcao_consulta = input('Escolha a opção desejada: \n' +
                                '1- Consultar Todos os Funcionários\n' +
                                '2- Consultar Funcionário por ID\n' +
                                '3- Consultar Funcionário por SETOR\n' +
                                '4- Retornar\n' +
                                '>> '
                               )
        if opcao_consulta == '1':
            for funcionario in funcionarios:# para cada item da lista (o objeto funcionario que adicionamos)
                print('-'*20)
                #  O objeto view, retornado por items(), contém os pares chave-valor do dicionário, como tuplas em uma lista
                for chave, valor in funcionario.items(): 
                    print('{}: {}' .format(chave, valor))
                print('-'*20)
        elif opcao_consulta == '2':
            codigo_desejado = int (input('Entre com o ID do funcionário'))
            for funcionario in funcionarios:
                if funcionario['id'] == codigo_desejado:
                    print('-'*20)
                    for chave, valor in funcionario.items():
                        print('{}: {}' .format(chave, valor))
                    print('-'*20)
        elif opcao_consulta == '3':
            codigo_desejado = input('Entre com o setor do funcionário')
            for funcionario in funcionarios:
                if funcionario['setor'] == codigo_desejado:
                    print('-'*20)
                    for chave, valor in funcionario.items():
                        print('{}: {}' .format(chave, valor))
                    print('-'*20)
        elif opcao_consulta == '4':
            return # sai da função e retorna para o cógigo principal
        else: # se digitar algo diferente das opções dadas
            print('Opção inválida, tente novamente.')
            continue # enquanto ele não digitar correto, pra sair ou escolher uma opção, vai ficar retornando pro início da consulta


# funcao para remover funcionario
def remover_funcionario():
    print('*'*100)
    print('-'*33,'Menu de remoção de funcionários','-'* 33)
    codigo_desejado = int(input('Entre com o ID do funcionário a ser removido do banco de dados: '))
    for funcionario in funcionarios:
        if funcionario['id'] == codigo_desejado:
            funcionarios.remove(funcionario)
            print('Funcionário Removido')

print('-'*100)
print('Bem vindo ao Sistema de Gestão de Banco de Dados de Funcionário do Davi Henrique')
while True:
    print('*'*100)
    print('-'*42, 'Menu Principal','-'*42)
    opcao = input ('Escolha a opção desejada: \n' +
                    '1- Cadastrar Funcionário\n' +
                    '2- Consultar Funcionário\n' +
                    '3- Remover Funcionário\n' +
                    '4- Sair\n' +
                    '>> '
                   )
    if opcao == '1':
        id_funcionario += 1 # adiciona +1 ao contador do ultimo usuário
        cadastrar_funcionario(id_funcionario)
    elif opcao == '2':
        consultar_funcionario()
    elif opcao == '3':
        remover_funcionario()
    elif opcao == '4':
        break # encerra aqui
    else: # se digitou qualquer coisa que não seja uma das opções dadas
        print('Opção inválida. Tente Novamente')
        continue