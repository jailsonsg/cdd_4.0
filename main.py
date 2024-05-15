#Programa que solicita o nome do aluno,suas notas. Faz o cálculo e exibe a media do aluno.
nomeAluno = input("Digite o nome do aluno:")
#O input sempre trata os dados como string. Para realizar calculos usando os dados capitados pelo input, precisa usar a função float.
nota1 = float(input("Digite sua 1 nota: "))
nota2 = float(input("Digite sua 2 nota: "))
media = (nota1+nota2) / 2
print(f"A média de {nomeAluno} é {media}")

