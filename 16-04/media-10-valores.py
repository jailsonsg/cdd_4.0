somaNotas = 0
qtdNotas = 0
for contador in range(10):
    notas = float(input("Digite uma nota: "))
    if notas >= 0 and notas <= 10:
        somaNotas = somaNotas + notas
        qtdNotas = qtdNotas + 1
    else:
        print("A nota digitada não esta no intervalo entre 0 e 10.")
media = somaNotas / qtdNotas
print(f"A media dos números digitados é : {media}")

