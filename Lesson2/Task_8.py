"""Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!"."""

from flask import Flask, render_template, redirect, url_for, request, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = 'ваш_секретный_ключ'

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get('name')
        flash(f'Привет, {name}!')
        return redirect(url_for("namehello"))
    else:
        return render_template("helloname.html")

@app.route('/namehello', methods=["GET", "POST"])
def namehello():
    messages = get_flashed_messages()
    return render_template("hello_myfrend.html", messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
