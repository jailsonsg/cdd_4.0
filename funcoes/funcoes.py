#criando a função
def piramide(numero):
    for x in range(1,numero+1):
        for y in range(1,x+1):
            print(x, end=" ")
        print()

#usando a funcao criada (chamando)
'''opcao = int(input("Digite um numero: "))
piramide(opcao)'''

# parametro é uma variavel interna da funcao
def piramide2(n):
    #For para pecorrer as linhas (começa com 1, vai até o numero digitado + 1, de 1 em 1)
    for linha in range(1,n+1,1):
        #For para percorrer as colunas (começa com 1, vai ate a quantidade de linhas + 1, de 1 em 1)
        for coluna in range(1,linha+1):
            #mostrar a coluna e
            print(coluna, end=" ")
        print()

'''n = int(input("Digite um numero: "))
piramide2(n)'''

texto = "o rato roeu a roupa do rei de roma"
#print("O tamanho é",len(texto))

'''vogais = 0
for x in range(len(texto)):
    if texto[x] == "a" or texto[x] == "e" or texto[x] == "i" or texto[x] == "o" or texto[x] == "u":
        vogais = vogais + 1
print("A frase tem", vogais, "vogais." )'''


def palavra(texto):
    cont = 0
    vogais = "aeiouAEIOU"
    for x in texto:
        if x in vogais:
            cont = cont +1
    print("A frase tem:",cont, "vogais")


#palavra(texto)


def estoque(nome_produto,quantidade_estoque,valor_unitario):
    valortotal = quantidade_estoque * valor_unitario
    return valortotal


#nomeDoProduto = input("Digite o nome do produto: ")
#quantidadeDeProdutos = int(input("Digite a quantidade de produtos: "))
#valorDosProdutos = float(input("Digite o valor unitário do produto: "))

#valorArroz = estoque(nomeDoProduto,quantidadeDeProdutos,valorDosProdutos)
#print(valorArroz)

def verificaNumero(numero):
    if numero > 0:
        return "P"
    elif numero < 0:
        return "N"
    else:
        return "Z"
#numero = int(input("Digite um numero: "))
#verificaNumero(numero)

produtos = []
precos = []


def estoque2(nome,preco):
    produtos.append(nome)
    precos.append(preco)

def somar(argumento_1,argumento2):
    soma = argumento_1 + argumento2
    return soma
