"""Задание №4
Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом"""

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
         # Получение значения из поля ввода пароля (если нужно)
        text_input = request.form.get('text_input')  # Получение значения из поля ввода текста

        # Ваша логика обработки данных

        return render_template("success.html", text_input=text_input)  # Переход на страницу успеха с передачей текста
    else:
        return render_template("masege.html")  # Отображение формы для ввода текста

if __name__ == '__main__':
    app.run(debug=True)
