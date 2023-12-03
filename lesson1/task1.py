
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """Я не смотрел семинар, я был занят в поездках.<br>
Я решил делать все задания в этотv вебприложении:<br>
под разными страницицы вебпреложения это задания по порядку"""


"""Задание №1
Напишите простое веб-приложение на Flask, которое будет
выводить на экран текст "Hello, World!"."""

@app.route('/HelWor/')
def hello_world():
    return "Hello, World!"
    # return 42

"""Добавьте две дополнительные страницы в ваше вебприложение:
○ страницу "about"
○ страницу "contact"."""

@app.route("/about/")
def about():
    return f"здесь могла быть ваша реклама"

@app.route("/contact/")
def contact():
    return f"здесь могла быть ваша реклама"

if __name__ == "__main__":
    app.run(debug=True)