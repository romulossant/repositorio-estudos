def inserir_nome_no_bd():
    while True:
        caractere_invalido = False

        nome = str(input("Digite o nome: "))
        for letra in nome:
            if letra.isdigit() == True:
                caractere_invalido = True
                print("Caracter inválido no nome. Insira novamente.\n")
        if caractere_invalido == False:
            return nome.upper()
        
def inserir_idade_no_bd():
    while True:
        idade = (input("Digite a idade: "))
        if idade.isdecimal() == True:
            return idade
        else:
            print("Idade inválida. Insira novamente.\n")

def inserir_genero_no_bd():
    genero = None

    while True:
        genero = str(input("Insira o gênero [M/F]: "))
        if genero.upper() == "M":
            return("MASCULINO")
        elif genero.upper == "F":
            return("FEMININO")
        
def inserir_dados_no_bd():
    nome = inserir_nome_no_bd()
    idade = inserir_idade_no_bd()
    genero = inserir_genero_no_bd()
    
    confirma = str(input(""))
    