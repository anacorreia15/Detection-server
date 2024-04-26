import mysql.connector
from mysql.connector import Error

def conect_bd():
    # Configurações de conexão com o banco de dados
    config = {
        'host' : 'localhost',
        'user' : 'user',
        'password' : 'senha',
        'database' : 'test'
    }

    try:
        # Conectar à base de dados
        conexao = mysql.connector.connect(**config)
        print("Conexão bem sucedida!")
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None
    
def insert_table(conexao, data_atual, volume_sopa_desperdicado):
    try:
        cursor = conexao.cursor()
        # Comando SQL para inserir dados na tabela refeicao
        sql_insert = "INSERT INTO refeicao (data, volume_sopa_desperdicado) VALUES (%s, %s)"
        # Dados a serem inseridos
        dados = (data_atual, volume_sopa_desperdicado)
        # Executar o comando SQL
        cursor.execute(sql_insert, dados)
        # Confirmar a transação
        conexao.commit()
        print("Dados inseridos com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao inserir dados na tabela refeicao: {erro}")
    finally:
        if cursor:
            cursor.close()

# Exemplo de utilização:
#conexao = conect_bd()
# if conexao:
#     # Realizar operações no banco de dados
#conexao.close()  # Fechar a conexão quando terminar de usar
