import sqlite3 as sql
import databases as db

class Pessoa:
    def __init__(self, nome = None, idade = None, genero = None):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def inserir_nome(self):
        while True:
            self.nome = str(input("Digite o nome: "))
            # remove os espaços das extremidades do nome e retira todos os espaços do nome para validar  
            # se existem apenas letras ou se existe algum caractere indesejado no meio
            nome_valido = self.nome.strip()
            nome_valido = nome_valido.replace(" ", "")

            if nome_valido.isalpha():
                return self.nome.upper()
            else:
                print("Existem caracteres inválidos ou o nome está em branco. Digite novamente.")
            
    def inserir_idade(self):
        while True:
            self.idade = (input("Digite a idade (apenas número): "))
            if self.idade.isdecimal():
                return self.idade
            else:
                print("Idade inválida. Insira novamente.")

    def inserir_genero(self):
        while True:
            genero = str(input("Insira o gênero [M/F]: "))
            if genero.upper() in ["M", "F"]:
                return "MASCULINO" if genero.upper() == "M" else "FEMININO"
            print("Gênero inválido. Insira novamente.")

    def confirmar_insercao(nome, idade, genero):
        confirma = str(input(f"\n{nome}, {idade} ANOS, {genero}.\nDeseja confirmar o cadastro? [S/N]: ")).upper()
        return True if confirma.upper() == "S" else False
        
    def inserir_pessoa(self):
        self.nome = Pessoa.inserir_nome(self)
        self.idade = Pessoa.inserir_idade(self)
        self.genero = Pessoa.inserir_genero(self)
        # confirmação se quer mesmo inserir a pessoa no banco de dados
        if Pessoa.confirmar_insercao(self.nome, self.idade, self.genero):
            db.cursor.execute(F"INSERT INTO nome_da_tabela VALUES {self.nome, self.idade, self.genero}")
            db.banco.commit()
            print(f"Cadastro realizado com sucesso.")