nomeTime1 = input("Digite o nome do primeiro time: ")
golsTime1 = int(input("Digite os gols do time 1: "))
nomeTime2 = input("Digite o nome do segundo time: ")
golsTime2 = int(input("Digite os gols do time 2: "))
if golsTime1 > golsTime2 :
    print(f"VENCEDOR : {nomeTime1}")
elif golsTime2 > golsTime1:
    print(f"VENCEDOR : {nomeTime2}")
else:
    print("EMPATE")
