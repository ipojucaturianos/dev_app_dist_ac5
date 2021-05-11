from flask import render_template, request, redirect, url_for
from app.model.utils import busca_logradouro
from app import app, db
from app.model.tables import Ipojucaturianos

@app.route("/")
def index():
    alunos = Ipojucaturianos.query.all()
    return render_template("index.html", alunos=alunos)

@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        logradouro = busca_logradouro(request.form['cep'])
        aluno = Ipojucaturianos(
            request.form['nome'],
            request.form['email'],
            logradouro,
            request.form['numero'],
            request.form['cep'],
            request.form['complemento']
        )
        db.session.add(aluno)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route("/edit/<int:ra>", methods=['GET','POST'])
def edit(ra):
    aluno = Ipojucaturianos.query.get(ra)
    if request.method == 'POST':
        aluno.nome = request.form['nome']
        aluno.email = request.form['email']
        aluno.cep = request.form['cep']
        aluno.numero = request.form['numero']
        aluno.complemento = request.form['complemento']
        aluno.logradouro = busca_logradouro(aluno.cep)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', aluno=aluno)

@app.route("/delete/<int:ra>")
def delete(ra):
    aluno = Ipojucaturianos.query.get(ra)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('index'))
