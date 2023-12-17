"""Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом."""


from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect(url_for("calculate"))
    else:
        return render_template("numbers_form.html")

@app.route('/calculate', methods=["POST"])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    
    # Выполните вычисления в зависимости от выбранной операции
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == "multiplication":
        result = num1 * num2
    elif operation == "division":
        result = num1 / num2
    else:
        result = 'Неверная операция'

    return render_template("calculate_result.html", num1=num1, num2=num2, operation=operation, result=result)


if __name__ == '__main__':
    app.run(debug=True)
