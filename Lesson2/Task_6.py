"""Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста."""



from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect(url_for("authentication"))
    else:
        return render_template("agename.html")

@app.route('/authentication', methods=["POST"])
def authentication():
    age = int(request.form['age'])
    name = request.form['name']
    result = ""
    
    
    if age <= 18:
        result = "вам нельзя войти"
    else:
        result = "вы мождете войти"

    return render_template("authentication_result.html", age=age, name=name, result=result)


if __name__ == '__main__':
    app.run(debug=True)
