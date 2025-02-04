#   números pares de 0 até 20
def num_pares_0a20():
    pares = [numero for numero in range(20) if numero % 2 == 0]
    print(pares)

#   quadrados dos numeros de 1 a 10
def quadrados_0a10():
    quadrados = [numero ** 2 for numero in range(10)]
    print(quadrados)

#   filtro de strings, filtrar palavras com 5 letras ou mais e que comece com p
def filtro_maior_5letras():
    palavras = ["python", "programação", "desafio", "list", "comprehension"]
    maior_5_letras = [palavra for palavra in palavras if len(palavra) > 5 and palavra[0] == 'p']
    print(maior_5_letras)

#   números divisíveis por 3 e 5
def divisiveis_3e5():
    divisiveis = [numero for numero in range(100) if numero % 5 == 0 and numero % 3 == 0]
    print(divisiveis)

#   inverter strings
def inverter_strings():
    frutas = ["maçã", "banana", "laranja", "uva"]
    strings_invertidas = [fruta[::-1] for fruta in frutas]
    print(strings_invertidas)

#   lista de tuplas, que contém um número e seu quadrado dentro da tupla, ex: [(1,1), (3,9)]
def lista_de_tuplas():
    numeros = [1,2,3,4,5]
    lista_tuplas = [(num, num ** 2) for num in numeros]
    print(lista_tuplas)

if __name__ == "__main__":
    num_pares_0a20()
    quadrados_0a10()
    filtro_maior_5letras()
    divisiveis_3e5()
    inverter_strings()
    lista_de_tuplas()