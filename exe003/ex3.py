# função para receber metragem da limpeza
def metragem_limpeza():
    print('|--------------------------------------------------------|')
    print('                  Metragem da Limpeza')
    print('|--------------------------------------------------------|')
    print('\n')
    while True:
        try:
            metragemL = int(input('Digite a metragem da limpeza (valor entre 30 e 699m2): '))
            if(metragemL >= 30) and (metragemL < 300): # Se a metragem estiver entre 30m² e 299m², retorne:
                print('É necessário contratar uma pessoa.')
                return metragemL * 0.3 + 60
            elif (metragemL >= 300) and (metragemL < 700): # Se a metragem estiver entre 300m² e 699m², retorne
                print('É necessário contratar duas pessoas')
                return metragemL * 0.5 + 120
            else: # Se o usuário digitar um valor menor que 30 ou maior que 699:
               print('Valor inválido.')
               continue # retorna para a pergunta
        except ValueError: # caso o usuário digite uma letra ou um número decimal
            print('digite um número válido e inteiro')

# função para receber o tipo da limpeza
def tipo_limpeza():
    print('|--------------------------------------------------------|')
    print('                    Tipo de Limpeza')
    print('|--------------------------------------------------------|')
    print('\n')
    while True:
        tipoL = input('Digite o tipo de limpeza desejada: \n' +
                      'B - Básica - Indicada para sujeiras semanais ou quinzenais \n' +
                      'C - Completa - Indicada para sujeiras antigas e/ou não rotineiras \n' +
                      '>> ') # caso o usuário digite minúsculas, e depois remove os espaços em branco da string
        tipoL = tipoL.upper()
        tipoL = tipoL.strip()
        if (tipoL == 'B'):
            return 1.00 # para multiplicar o valor por 1, retornando ele mesmo
        elif (tipoL == 'C'):
            return 1.30 # aumento de 30%
        else:
            print('Por favor, humano! Digite B ou C!')
            continue # retorna para o início


# função adicional_limpeza
def adicional_limpeza():
    print('|--------------------------------------------------------|')
    print('                   Opções Adicionais')
    print('|--------------------------------------------------------|')
    print('\n')
    acumulador = 0
    while True:
        adicional = input('Deseja adicionar algum serviço extra? \n' +
                          '0- Não desejo mais nada (encerrar) \n' +
                            '1- Passar 10 peças de roupas - R$ 10.00 \n' +
                            '2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00 \n' +
                            '3- Limpeza de 1 Geladeira/Freezer - R$ 20,00 \n' +
                            '>> ')
        if (adicional == '0'):
            return acumulador # não adicionou nada
        elif (adicional == '1'):
            acumulador = acumulador + 10
            continue # volta para perguntar se quer adicionar mais coisas
        elif (adicional == '2'):
            acumulador = acumulador + 12
            continue
        elif (adicional == '3'):
            acumulador = acumulador + 20
            continue

print('* Bem Vindo ao sistema de serviço de limpeza do Davi Henrique')
metragem = metragem_limpeza() # armazenando o retorno das funçõe em variáveis
tipo = tipo_limpeza()
adicionais = adicional_limpeza()

total = metragem * tipo + adicionais
print('Total: R${:.2f} (metragem: {:.2f}m² * tipo: {:.2f} + total adicionais: R${:.2f})' .format(total, metragem, tipo, adicionais))