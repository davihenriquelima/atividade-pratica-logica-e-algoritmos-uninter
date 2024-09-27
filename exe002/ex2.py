print('Bem-Vindo à Sorveteria do Davi Henrique')

print('---------------------------------------------Cardápio---------------------------------------------')
print('|  Código   | Descrição            | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (1500ml) |')
print('|    TR     | Sabores Tradicionais |      R$ 6,00      |      R$ 10,00      |      R$ 18,00      |')
print('|    ES     | Sabores Especiais    |      R$ 7,00      |      R$ 12,00      |      R$ 21,00      |')
print('|    PR     | Sabores Premium      |      R$ 8,00      |      R$ 14,00      |      R$ 24,00      |')
print('--------------------------------------------------------------------------------------------------')

valor = 0

while True:
    tam = input('Digite o tamanho do pote desejado (P/M/G): ')
    tam = tam.upper() #convertendo os caracteres de entrada para maiúsculo
    if tam!='P' and tam!='M' and tam!='G': #se o tamanho for diferente de P, M ou G
        print('Este pote não existe. Código ou Tamanho inválidos!. Tente Novamente')
        continue #retorne ao início
    cod = input('Digite o código do seu delicioso sorvete (TR/ES/PR: )')
    cod = cod.upper() #convertendo os caracteres de entrada para maiúsculo
    if cod!='TR' and cod!='ES' and cod!='PR':
        print('Este pote não existe. Código ou Tamanho inválidos! Tente Novamente')
        continue
    
    if cod == 'TR' and tam == 'P':
        print('Você escolheu o pote do tipo Sabores Tradicionais tamanho P (500ml) de R$6.00')
        print('------------------------------------------------------------------------------')
        valor = valor + 6 #adicionando o valor dos itens ao acumulador
    elif cod == 'TR' and tam == 'M':
        print('Você escolheu o pote do tipo Sabores Tradicionais tamanho M (1000ml) de R$10.00')
        print('------------------------------------------------------------------------------')
        valor = valor + 10
    elif cod == 'TR' and tam == 'G':
        print('Você escolheu o pote do tipo Sabores Tradicionais tamanho G (1500ml) de R$18.00')
        print('------------------------------------------------------------------------------')
        valor = valor + 18
    elif cod == 'ES' and tam == 'P':
        print('Você escolheu o pote do tipo Sabores Especiais tamanho P (500ml) de R$7.00')
        print('------------------------------------------------------------------------------')
        valor = valor + 7
    elif cod == 'ES' and tam == 'M':
        print('Você escolheu o pote do tipo Sabores Especiais tamanho M (1000ml) de R$12.00')
        print('------------------------------------------------------------------------------')
        valor = valor + 12
    elif cod == 'ES' and tam == 'G':
        print('Você escolheu o pote do tipo Sabores Especiais tamanho G (1500ml) de R$21.00')
        print('------------------------------------------------------------------------------')
        valor = valor + 21
    elif cod == 'PR' and tam == 'P':
        print('Você escolheu o pote do tipo Sabores Premium tamanho P (500ml) de R$8.00')
        print('------------------------------------------------------------------------------')
        valor = valor + 8
    elif cod == 'PR' and tam == 'M':
        print('Você escolheu o pote do tipo Sabores Premium tamanho M (1000ml) de R$14.00')
        print('------------------------------------------------------------------------------')
        valor = valor + 14
    elif cod == 'PR' and tam == 'G':
        print('Você escolheu o pote do tipo Sabores Premium tamanho G (1500ml) de R$24.00')
        print('------------------------------------------------------------------------------')
        valor = valor + 24
    
    adicionarAoCarrinho = input('Deseja pedir mais deliciosos potes de sorvete? (S para sim ou digite qualquer tecla para Não): ')
    adicionarAoCarrinho = adicionarAoCarrinho.upper()

    if adicionarAoCarrinho == 'S':
        continue #se o usuário digitar sim, volte à entrada inicial
    else:
        print('Total a ser pago: R${:.2f}' .format(valor))
    break