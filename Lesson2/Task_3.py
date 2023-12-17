"""Создать страницу, на которой будет форма для ввода логина
и пароля
При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой."""
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        if login == "admin" and password == "qerty":
            return redirect(url_for("hello", login=login))
        else:
            return redirect(url_for("error"))
    else:
        return render_template("autontif.html")

@app.route('/error/')
def error():
    return render_template("error.html")

@app.route('/hello/<string:login>')
def hello(login):
    return render_template("hello.html", name=login)

if __name__ == '__main__':
    app.run(debug=True)
