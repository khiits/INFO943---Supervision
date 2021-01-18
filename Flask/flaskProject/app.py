from flask import Flask, render_template, request
import datetime


def create_app():
    app = Flask(__name__)  # type: Flask

    @app.route('/')
    def homepage():
        return render_template('homepage.html')

    @app.route('/about/')
    def about():
        return render_template('about.html')

    @app.route('/formulaire/')
    def formulaire():
        return render_template('formulaire.html')

    @app.route('/hello/')
    @app.route('/hello/<name>/')
    def hello(name='Vincent'):
        return render_template('hello.html', name=name)

    @app.route('/resultat/', methods=['POST'])
    def resultat():
        result = request.form
        n = result['nom']
        p = result['prenom']
        return render_template("resultat.html", nom=n, prenom=p)

    return app