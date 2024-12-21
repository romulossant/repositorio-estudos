import os
import sqlite3 as sql
import databases

class Pessoa:
    def __init__(self, nome = "", idade = "", genero = ""):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def inserir_nome(self):
        while True:

            self.nome = str(input("Digite o nome: "))
            nome_valido = self.nome
            nome_valido.replace(" ", "")

            if nome_valido.isalpha():
                return self.nome.upper()
            else:
                print("Existem caracteres inválidos ou o nome está em branco. Digite novamente.")
            
            # while True:
            # nome_valido = True

            # self.nome = str(input("Digite o nome: "))
            # # validação se o nome está em branco
            # if self.nome.strip() == "":
            #     nome_valido = False
            #     print("O nome não pode estar em branco. Digite novamente.")
            # # validação se existem caracteres indesejados no nome, como numeros
            # for letra in self.nome:
            #     if letra.isdigit():
            #         nome_valido = False
            #         print("Existem caracteres inválidos no nome. Digite novamente.")
            #         break

            # if nome_valido:
            #     return self.nome.upper()



    def inserir_idade(self):
        while True:
            self.idade = (input("Digite a idade: "))
            if self.idade.isdecimal() == True:
                return self.idade
            else:
                print("Idade inválida. Insira novamente.")

    def inserir_genero(self):
        genero = None

        while True:
            genero = str(input("Insira o gênero [M/F]: "))
            if genero.upper() in ["M", "F"]:
                return "MASCULINO" if genero.upper() == "M" else "FEMININO"
            print("Gênero inválido. Insira novamente.")
        
        
    def inserir_pessoa(self):
        self.nome = Pessoa.inserir_nome(self)
        self.idade = Pessoa.inserir_idade(self)
        self.genero = Pessoa.inserir_genero(self)
