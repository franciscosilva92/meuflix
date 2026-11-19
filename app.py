import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DATABASE = 'catalogo.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS midias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            tipo TEXT NOT NULL,
            genero TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL,
            imagem_url TEXT NOT NULL,
            sinopse TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Chama a criação da tabela sempre que o app iniciar
init_db()

# ROTA 1: Página Inicial (Vitrine estilo Netflix)
@app.route('/')
def index():
    conn = get_db_connection()
    filmes = conn.execute("SELECT * FROM midias WHERE tipo = 'Filme' ORDER BY id DESC").fetchall()
    series = conn.execute("SELECT * FROM midias WHERE tipo = 'Série' ORDER BY id DESC").fetchall()
    destaque = conn.execute("SELECT * FROM midias ORDER BY nota DESC LIMIT 1").fetchone()
    conn.close()
    return render_template('index.html', filmes=filmes, series=series, destaque=destaque)

# ROTA 2: Cadastrar Novo Filme/Série
@app.route('/adicionar', methods=('GET', 'POST'))
def adicionar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        tipo = request.form['tipo']
        genero = request.form['genero']
        ano = request.form['ano']
        nota = request.form['nota']
        imagem_url = request.form['imagem_url']
        sinopse = request.form['sinopse']

        conn = get_db_connection()
        conn.execute('''
            INSERT INTO midias (titulo, tipo, genero, ano, nota, imagem_url, sinopse)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (titulo, tipo, genero, ano, nota, imagem_url, sinopse))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('form.html', midia=None)

# ROTA 3: Editar Filme/Série Existente
@app.route('/editar/<int:id>', methods=('GET', 'POST'))
def editar(id):
    conn = get_db_connection()
    midia = conn.execute('SELECT * FROM midias WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        titulo = request.form['titulo']
        tipo = request.form['tipo']
        genero = request.form['genero']
        ano = request.form['ano']
        nota = request.form['nota']
        imagem_url = request.form['imagem_url']
        sinopse = request.form['sinopse']

        conn.execute('''
            UPDATE midias 
            SET titulo = ?, tipo = ?, genero = ?, ano = ?, nota = ?, imagem_url = ?, sinopse = ?
            WHERE id = ?
        ''', (titulo, tipo, genero, ano, nota, imagem_url, sinopse, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('form.html', midia=midia)

# ROTA 4: Deletar Filme/Série
@app.route('/deletar/<int:id>', methods=('POST',))
def deletar(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM midias WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()  # Garante que o banco existe antes de iniciar
    app.run(debug=True)