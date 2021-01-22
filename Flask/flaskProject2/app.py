
from flask import Flask, render_template, request, g
import sqlite3

def create_app():
    app = Flask(__name__)  # type: Flask

    @app.route('/')
    def homepage():
        return render_template('formulaire.html')

    @app.route('/about/')
    def about():
        return render_template('about.html')

    @app.route('/reg',methods=['GET', 'POST'])
    def formulaire():
        connexion = sqlite3.connect("identifier.sqlite")
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            cursor = connexion.cursor()
            cursor.execute("INSERT INTO form(username, password) VALUES(?, ?)", (str(username), str(password)))
            connexion.commit()
            connexion.close()
            return render_template('formulaire.html')

    @app.route('/hello/')
    @app.route('/hello/<name>/')
    def hello(name='Vincent'):
        return render_template('hello.html', name=name)

    @app.route('/log', methods=['GET', 'POST'])
    def resultat():
        connexion = sqlite3.connect("identifier.sqlite")
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            cursor = connexion.cursor()
            cursor.execute("SELECT username, password FROM form WHERE username=? AND password=?", (str(username), str(password)))
            info = cursor.fetchone()
            if info[0] == username and info[1] == password:
                connexion.close()
                return render_template('resultat.html')
            else:
                return "login unsuccessful, please register"


    @app.route('/new')
    def register():
            return render_template('register.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.debug = True
    app.run()