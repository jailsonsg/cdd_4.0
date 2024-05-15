#Ler 10 valores e escrever quantos desses valores lidos estão no intervalo de (10-20)
## Incluindo os valores 10 e 20 no intervalo.
##Quantos deles estão fora deste intervalo.
dentroDoIntervalo = 0
foraDOIntervalo = 0

for contador in range(0,10,1):
    numero = int(input("Digite um número: "))
    if numero >= 10 and numero <= 20:
        dentroDoIntervalo += 1
    else:
        foraDOIntervalo += 1
print(f"{dentroDoIntervalo} números estão dentro do intervalo. e {foraDOIntervalo} números estão fora do intervalo.")