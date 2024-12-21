import sqlite3 as sql
import os

# BIBLIOTECA OS
# a biblioteca os serve pra fazer manipulação de arquivos no sistema operacional, eu vou utilizar
# ela pra fazer a criação do banco de dados dentro da pasta que eu quero, que no caso é a 
# aprendendo_sqlite3. os.getcwd() serve pra pegar o diretório da pasta raiz do seu programa
# e a constante PASTA_APRENDENDO_SQLITE é o nome da pasta. 
PASTA_PRINCIPAL = os.getcwd()
PASTA_APRENDENDO_SQLITE = "aprendendo_sqlite3"

# CRIAÇÃO DO BANCO DE DADOS
# para fazer a criação do banco de dados cria-se uma variável e usa o método .connect
# com o nome do arquivo dentro de parênteses. NÃO ESQUECER O .db no final. os.path.join()
# serve pra fazer a criação do diretório que você quer, concatenando as constantes e o nome
# do banco de dados da sua escolha. o nome também pode ser definido como uma variável qualquer
NOME_BD = os.path.join(PASTA_PRINCIPAL, PASTA_APRENDENDO_SQLITE, "BANCO.db")
banco = sql.connect(NOME_BD)

# CRIAÇÃO DAS TABELAS DO BANCO DE DADOS
# antes, vc precisa criar o CURSOR, ele é o objeto que te permite executar comandos dentro do
# banco de dados e manipular ele.
# IF NOT EXISTS
# esse if not exists serve pra fazer uma verificação quando você quer criar uma nova tabela
# se você colocar o programa pra criar uma tabela que já exist ele vai dar erro, então é bom
# colocar essa verificação pra não dar quebrar o código
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS nome_da_tabela (nome text, \
               idade integer, genero text)")


