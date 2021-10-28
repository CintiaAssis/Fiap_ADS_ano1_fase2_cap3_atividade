#Olhando para o mercado de educação infantil, você e sua equipe decidem criar um aplicativo onde as crianças aprendam a controlar os seus gastos.
#Como forma de validar um protótipo, foi solicitado que você crie um script simples,
#em que o usuário deve informar QUANTAS TRANSAÇÕES financeiras realizou ao longo de um dia e, na sequência, deve informar o VALOR DE CADA UMA das transações que realizou.
#Seu programa deverá exibir, ao final, o valor total gasto pelo usuário e também a média do valor de cada transação.

quantidade_compras = int(input('Quantas compras você fez hoje: '))
compra = 1
total = 0
for x in range(quantidade_compras):
    compra = float(input('Informe o valor da compra: '))
    total = total + compra
    media = total / quantidade_compras
print("Hoje você gastou um total de R$ {:.2f}".format(total))
print("Sua media por compra foi de R$ {:.2f}".format(media))

