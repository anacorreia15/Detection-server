import mysql.connector
from mysql.connector import Error
from random import randint, random
from datetime import datetime, timedelta
import db_handler

conection = db_handler.conect_bd()

def insert_table(conexao, data_atual, volume_sopa_desperdicado, tigela):
    try:
        # Preparar o cursor
        cursor = conexao.cursor()

        # Comando SQL para inserir dados na tabela refeicao
        sql_insert = "INSERT INTO refeicao (data, volume_sopa_desperdicado, tigela) VALUES (%s, %s, %s)"

        # Dados a serem inseridos
        dados = (data_atual, volume_sopa_desperdicado, tigela)

        # Executar o comando SQL
        cursor.execute(sql_insert, dados)

        # Confirmar a transação
        conexao.commit()

    except mysql.connector.Error as erro:
        print(f"Erro ao inserir dados na tabela refeicao: {erro}")

    finally:
        # Fechar o cursor
        if cursor:
            cursor.close()

# Função para gerar um volume aleatório entre 0.0 e 0.3 litros
def generate_random_volume():
    return round(random() * 0.3, 2)

# Função para gerar um valor booleano aleatório (0 ou 1)
# Função para gerar um valor booleano aleatório com mais 1s do que 0s
def generate_random_boolean():
    # Definir uma probabilidade de gerar 1
    probability_of_one = 0.65  # Por exemplo, 65% de chance de gerar 1
    if random() < probability_of_one:
        return 1
    else:
        return 0


# Início e fim do período de tempo desejado (janeiro a maio de 2024)
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 5, 31)

# Número de registros a serem inseridos para cada dia
num_registros_por_dia = 10

if conection is not None:
    # Iterar por cada dia no período de tempo
    current_date = start_date
    while current_date <= end_date:
        for _ in range(num_registros_por_dia):
            data_atual = current_date.strftime('%Y-%m-%d')
            volume_sopa_desperdicado = generate_random_volume()
            tigela = generate_random_boolean()
            insert_table(conection, data_atual, volume_sopa_desperdicado, tigela)
        # Avançar para o próximo dia
        current_date += timedelta(days=1)
else:
    print("Não foi possível estabelecer conexão à base de dados.")
