contador = 0
somaNotas = 0
divisao = 0
media = 0
quantidadeDeAlunos = int(input("Insira a quantidade de alunos: "))
while contador < quantidadeDeAlunos:
    notasDosAlunos = float(input(f"Digite a nota do aluno {contador}: "))
    if  notasDosAlunos >= 0 and notasDosAlunos <= 10:
      somaNotas = somaNotas + notasDosAlunos
      divisao = divisao + 1
      contador = contador + 1
media = (somaNotas/divisao)
print(f"A média dos alunos é: {media}")