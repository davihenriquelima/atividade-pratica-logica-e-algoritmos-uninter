print('Olá!, Bem-vindo ao Sistema de Vendas do Davi Henrique.')
print('Verificação do preço total do pedido pela quantidade do produto e embalagem para frete equivalente.')
print('Tabela de preços de embalagem para frete:')
print('De 0 a 10 produtos, a embalagem para frete custa R$30.00;')
print('De 11 a 100 produtos, a embalagem para frete custa R$60.00;')
print('De 101 a 1000 produtos, a embalagem para frete custa R$120.00;')
print('A partir de 1001 produtos, a embalagem para frete custa R$240.00;')

#solicitando o valor da unidade ao usuário
valorUnit = float(input('Digite o valor unitário do produto (usando "." para número decimal): '))

#solicitando a quantidade de unidades deste produto
qtdProduto = int(input('Agora digite a quantidade de unidades deste produto: '))

#definindo valores nos tipos de embalagem para frete
freteMenor = 30.00
freteMedio = 60.00
fretePremium = 120.00
freteSupremo = 240.00

if(0 <= qtdProduto < 11): #de 0 a 10 produtos, a embalagem para frete é R$30.00
    frete = freteMenor
    valorFinal = (valorUnit * qtdProduto) + frete
elif(11 <= qtdProduto < 101):#de 11 a 100 produtos, a embalagem para frete é R$60.00
    frete = freteMedio
    valorFinal = (valorUnit * qtdProduto) + frete
elif(101 <= qtdProduto < 1001):#de 101 a 1000 produtos, a embalagem para frete é R$120.00
    frete = fretePremium
    valorFinal = (valorUnit * qtdProduto) + frete
else: # a partir de 1001 produtos, o frete é R$240.00
    frete = freteSupremo
    valorFinal = (valorUnit * qtdProduto) + frete

print('Quantidade de unidades: {}' .format(qtdProduto))
print('Preço unitário: R${:.2f}' .format(valorUnit))
print('Valor do frete é: R${:.2f}' .format(frete))
print('O subtotal do pedido sem o frete é R${:.2f}' .format(valorUnit * qtdProduto))
print('O total do pedido com o frete é: R${:.2f}' .format(valorFinal))