'''
Crie uma função que recebe o nome de um produto, a quantidade que tem no estoque e o valor unitario do produto
retorne o valor total do meu estoque.
'''

prod = ["","","","",""]
prec = ["","","","",""]

for x in range(5):
    prod[x] = input("Insira o nome do produto: ")
for y in range(5):
    prec[y] = float(input("Insira o preco: "))

