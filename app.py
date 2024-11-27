from flask import Flask, render_template, request, redirect, url_for
from db import (
    get_donos, add_dono, get_dono, update_dono, delete_dono,
    get_animais, add_animal, get_animal, update_animal, delete_animal,
    get_consultas, add_consulta, get_consulta, update_consulta, delete_consulta
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Rotas para Donos
@app.route('/donos')
def donos():
    try:
        donos = get_donos()
    except Exception as e:
        return f"Erro ao carregar donos: {str(e)}", 500
    return render_template('donos.html', donos=donos)

@app.route('/donos/novo', methods=['GET', 'POST'])
def novo_dono():
    if request.method == 'POST':
        nome = request.form['nome'].strip()
        email = request.form['email'].strip()
        cpf = request.form['cpf'].strip()
        telefone = request.form['telefone'].strip()

        if not nome or not email or not cpf or not telefone:
            return "Todos os campos são obrigatórios", 400

        try:
            add_dono(nome, email, cpf, telefone)
            return redirect(url_for('donos'))
        except Exception as e:
            return f"Erro ao adicionar dono: {str(e)}", 500
    return render_template('novo_dono.html')

@app.route('/donos/editar/<int:id>', methods=['GET', 'POST'])
def editar_dono(id):
    dono = get_dono(id)
    if not dono:
        return f"Dono com ID {id} não encontrado.", 404
    if request.method == 'POST':
        nome = request.form['nome'].strip()
        email = request.form['email'].strip()
        cpf = request.form['cpf'].strip()
        telefone = request.form['telefone'].strip()

        if not nome or not email or not cpf or not telefone:
            return "Todos os campos são obrigatórios", 400

        try:
            update_dono(id, nome, email, cpf, telefone)
            return redirect(url_for('donos'))
        except Exception as e:
            return f"Erro ao atualizar dono: {str(e)}", 500
    return render_template('editar_dono.html', dono=dono)

@app.route('/donos/deletar/<int:id>')
def deletar_dono(id):
    dono = get_dono(id)
    if not dono:
        return f"Dono com ID {id} não encontrado.", 404
    try:
        delete_dono(id)
        return redirect(url_for('donos'))
    except Exception as e:
        return f"Erro ao deletar dono: {str(e)}", 500

# Rotas para Animais
@app.route('/animais')
def listar_animais():
    animais = get_animais()  # Chama a função para obter os animais do banco de dados
    return render_template('animais.html', animais=animais)

@app.route('/animais/novo', methods=['GET', 'POST'])
def novo_animal():
    if request.method == 'POST':
        nome = request.form['nome'].strip()
        tipo = request.form['tipo'].strip()
        idade = request.form['idade'].strip()
        peso = request.form['peso'].strip()
        especie = request.form['especie'].strip()
        dono_id = request.form['dono_id'].strip()

        if not nome or not tipo or not idade or not peso or not especie or not dono_id:
            return "Todos os campos são obrigatórios", 400

        try:
            add_animal(nome, tipo, idade, peso, especie, dono_id)
            return redirect(url_for('animais'))
        except Exception as e:
            return f"Erro ao adicionar animal: {str(e)}", 500
    donos = get_donos()
    return render_template('novo_animal.html', donos=donos)

@app.route('/animais/editar/<int:id>', methods=['GET', 'POST'])
def editar_animal(id):
    animal = get_animal(id)
    if not animal:
        return f"Animal com ID {id} não encontrado.", 404
    donos = get_donos()
    if request.method == 'POST':
        nome = request.form['nome'].strip()
        tipo = request.form['tipo'].strip()
        idade = request.form['idade'].strip()
        peso = request.form['peso'].strip()
        especie = request.form['especie'].strip()
        dono_id = request.form['dono_id'].strip()

        if not nome or not tipo or not idade or not peso or not especie or not dono_id:
            return "Todos os campos são obrigatórios", 400

        try:
            update_animal(id, nome, tipo, idade, peso, especie, dono_id)
            return redirect(url_for('animais'))
        except Exception as e:
            return f"Erro ao atualizar animal: {str(e)}", 500
    return render_template('editar_animal.html', animal=animal, donos=donos)

@app.route('/animais/deletar/<int:id>')
def deletar_animal(id):
    animal = get_animal(id)
    if not animal:
        return f"Animal com ID {id} não encontrado.", 404
    try:
        delete_animal(id)
        return redirect(url_for('animais'))
    except Exception as e:
        return f"Erro ao deletar animal: {str(e)}", 500

# Rotas para Consultas
@app.route('/consultas')
def consultas():
    try:
        consultas = get_consultas()
    except Exception as e:
        return f"Erro ao carregar consultas: {str(e)}", 500
    return render_template('consultas.html', consultas=consultas)

@app.route('/consultas/novo', methods=['GET', 'POST'])
def nova_consulta():
    if request.method == 'POST':
        data = request.form['data'].strip()
        descricao = request.form['descricao'].strip()
        animal_id = request.form['animal_id'].strip()

        if not data or not descricao or not animal_id:
            return "Todos os campos são obrigatórios", 400

        try:
            add_consulta(data, descricao, animal_id)
            return redirect(url_for('consultas'))
        except Exception as e:
            return f"Erro ao adicionar consulta: {str(e)}", 500
    animais = get_animais()
    return render_template('nova_consulta.html', animais=animais)

@app.route('/consultas/editar/<int:id>', methods=['GET', 'POST'])
def editar_consulta(id):
    consulta = get_consulta(id)
    if not consulta:
        return f"Consulta com ID {id} não encontrada.", 404
    animais = get_animais()
    if request.method == 'POST':
        data = request.form['data'].strip()
        descricao = request.form['descricao'].strip()
        animal_id = request.form['animal_id'].strip()

        if not data or not descricao or not animal_id:
            return "Todos os campos são obrigatórios", 400

        try:
            update_consulta(id, data, descricao, animal_id)
            return redirect(url_for('consultas'))
        except Exception as e:
            return f"Erro ao atualizar consulta: {str(e)}", 500
    return render_template('editar_consulta.html', consulta=consulta, animais=animais)

@app.route('/consultas/deletar/<int:id>')
def deletar_consulta(id):
    consulta = get_consulta(id)
    if not consulta:
        return f"Consulta com ID {id} não encontrada.", 404
    try:
        delete_consulta(id)
        return redirect(url_for('consultas'))
    except Exception as e:
        return f"Erro ao deletar consulta: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
