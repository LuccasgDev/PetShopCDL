import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="0703LT2023.",
        database="PetStoreDb"
    )

# Funções CRUD para Donos
def get_donos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, email, cpf, telefone FROM donos")
    donos = cursor.fetchall()
    cursor.close()
    conn.close()
    return donos

def add_dono(nome, email, cpf, telefone):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO donos (nome, email, cpf, telefone) VALUES (%s, %s, %s, %s)', 
                   (nome, email, cpf, telefone))
    conn.commit()
    conn.close()

def get_dono(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM donos WHERE id = %s', (id,))
    dono = cursor.fetchone()
    conn.close()
    return dono

def update_dono(id, nome, email, cpf, telefone):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE donos SET nome = %s, email = %s, cpf = %s, telefone = %s WHERE id = %s',
                   (nome, email, cpf, telefone, id))
    conn.commit()
    conn.close()

def delete_dono(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM donos WHERE id = %s', (id,))
    conn.commit()
    conn.close()

# Funções CRUD para Animais
def get_animais():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, tipo, idade, peso, especie, DonoId FROM animais")
    animais = cursor.fetchall()
    conn.close()
    return animais

def add_animal(nome, tipo, idade, peso, especie, dono_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO animais (nome, tipo, idade, peso, especie, DonoId) VALUES (%s, %s, %s, %s, %s, %s)', 
                   (nome, tipo, idade, peso, especie, dono_id))
    conn.commit()
    conn.close()

def get_animal(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM animais WHERE id = %s', (id,))
    animal = cursor.fetchone()
    conn.close()
    return animal

def update_animal(id, nome, tipo, idade, peso, especie, dono_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE animais SET nome = %s, tipo = %s, idade = %s, peso = %s, especie = %s, DonoId = %s WHERE id = %s',
                   (nome, tipo, idade, peso, especie, dono_id, id))
    conn.commit()
    conn.close()

def delete_animal(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM animais WHERE id = %s', (id,))
    conn.commit()
    conn.close()

# Funções CRUD para Consultas
def get_consultas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, data, descricao, animal_id FROM consultas")
    consultas = cursor.fetchall()
    conn.close()
    return consultas

def add_consulta(data, descricao, animal_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO consultas (data, descricao, animal_id) VALUES (%s, %s, %s)', 
                   (data, descricao, animal_id))
    conn.commit()
    conn.close()

def get_consulta(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM consultas WHERE id = %s', (id,))
    consulta = cursor.fetchone()
    conn.close()
    return consulta

def update_consulta(id, data, descricao, animal_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE consultas SET data = %s, descricao = %s, animal_id = %s WHERE id = %s',
                   (data, descricao, animal_id, id))
    conn.commit()
    conn.close()

def delete_consulta(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM consultas WHERE id = %s', (id,))
    conn.commit()
    conn.close()
