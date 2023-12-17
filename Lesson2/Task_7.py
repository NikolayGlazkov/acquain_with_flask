"""Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат."""


from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            num = int(request.form['num'])
            result = num ** 2
            return render_template("square_result.html", num=num, result=result)
        except ValueError:
            return render_template("error.html", message="Введите корректное число")
    else:
        return render_template("square.html")

if __name__ == '__main__':
    app.run(debug=True)

