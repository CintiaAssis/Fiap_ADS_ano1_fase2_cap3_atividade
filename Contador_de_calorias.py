#Uma das funções mais procuradas por usuários de aplicativos de saúde é o de controle de calorias ingeridas em um dia.
#Por essa razão, você deve elaborar um algoritmo implementado em Python em que o usuário informe
#quantos alimentos consumiu naquele dia e depois possa informar o número de calorias de cada um dos alimentos.
#Como não estudamos listas nesse capítulo você não deve se preocupar em armazenar todas as calorias digitadas,
#mas deve exibir o total de calorias no final.


quantidade_alimentos = int(input("Qual a quantidade de alimentos que você consumiu hoje? "))
calorias = 0
soma = 0
for x in range(quantidade_alimentos):
    calorias = float(input("Informe as calorias: "))
    soma = soma + calorias
print("Hoje você consumiu um total de {:.2f} calorias".format(soma))

