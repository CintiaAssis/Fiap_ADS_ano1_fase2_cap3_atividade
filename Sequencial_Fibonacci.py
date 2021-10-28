#Uma grande empresa de jogos está querendo tornar seus games mais desafiadores.
#Por isso ela contratou você para desenvolver um algoritmo que será aplicado futuramente em diversos outros games: o algoritmo da sorte de Fibonnaci.
#A ideia dessa empresa, é claro, é fazer com que seja mais difícil os jogadores terem sucesso nas ações que realizam nos games.
#Por isso o seu algoritmo deverá funcionar da seguinte forma: o usuário deve digitar um valor numérico inteiro e o algoritmo deverá verificar se esse valor encontra-se na sequência de Fibonnaci.
#Caso o número esteja na sequência, o algoritmo deve exibir a mensagem “Ação bem sucedida!” e, caso não esteja, deve exibir a mensagem “A ação falhou...”.

escolha_usuario = int(input("Escolha um numero: "))
sequencial_1 = 0
sequencial_2 = 1
numero_fibonacci = 0
while numero_fibonacci < escolha_usuario:
    numero_fibonacci = sequencial_2 + sequencial_1
    sequencial_1 = sequencial_2
    sequencial_2 = numero_fibonacci
if escolha_usuario == numero_fibonacci:
    print("Ação bem sucedida!")
else:
    print("A ação falhou...")
