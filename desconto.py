# Informe um valor e veja quanto de desconto você terá em R$, receba a % do desconto que quer receber;
print('Calculadora de descontos')
valor = float(input('Digite o valor em reais(R$): '))
porcento = int(input('Digite a porcentagem do desconto(%): '))
desconto = valor*(porcento/100)
desconto_total = valor-desconto
print(f'Ao todo, você irá economizar {desconto_total} reais.')