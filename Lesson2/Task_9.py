"""Создать страницу, на которой будет форма для ввода имени
и электронной почты
При отправке которой будет создан cookie файл с данными
пользователя
Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты."""


from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect(url_for("namehello"))
    else:
        return render_template("helloname.html")