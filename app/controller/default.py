from flask import render_template, request, redirect, url_for
from app import app, db
from app.model.tables import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        user = User(
            request.form['name'],
            request.form['email'],
            request.form['username'],
            request.form['password'],
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html')

@app.route("/signin", methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        request.form['username']
        request.form['password']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signin.html')

@app.route("/edit/<int:id>", methods=['GET','POST'])
def edit(id):
    user = User.query.get(id)
    if request.method == 'POST':
        user.form['name'],
        user.form['email'],
        user.form['password'],
        user.form['username'],
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', user=user)

@app.route("/delete/<int:id>")
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))
