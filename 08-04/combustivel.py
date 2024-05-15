precoDeG = 5.80
precoDeE = 4.90
tipoDoCombustivel = input("Digite o nome do combustível utilizado (G-gasolina ou E-etanol): ")
quantidadeDeLitros = float(input("Digite a quantidade de litros abastecidos: "))
#(OR) operador lógico, trata um caso ou trata outro caso.
if tipoDoCombustivel == "G" or tipoDoCombustivel == "g":
    print(f"O valor a ser pago é : {quantidadeDeLitros*precoDeG}")
elif tipoDoCombustivel == "E" or tipoDoCombustivel == "e":
    print(f"O valor a ser pago é: {quantidadeDeLitros*precoDeE}")
else:
    print("Tipo de combustivel inválido. Digite G (para gasolina) ou E (para etanol)")


