##Ler 10 valores e escrever quantos desses valores lidos são negativos.
negativos = 0
for contador in range(0,10,1):
    numero = int(input("Digite um número inteiro: "))
    if (numero < 0):
        negativos += 1
print(f"{negativos} números negativos foram digitados.")

##mudar o nome de variavel (em todos os lugares que ela estiver) botão direito > refactor > rename (Shit - f6).