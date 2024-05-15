#Programa que recebe 3 notas de um aluno, e verifique se ele esta aprovado ou reprovado.
#Considere que a média para aprovação é 7
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
media = (nota1+nota2+nota3) / 3
if media >= 7:
    print(f" A média do aluno foi {media}: APROVADO")
elif (media < 4):
    print(f" A média do aluno foi {media}: REPROVADO")
else:
    print(f"A média do aluno foi {media}: RECUPERAÇÃO")
