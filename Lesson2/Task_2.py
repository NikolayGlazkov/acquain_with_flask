"""Создать страницу, на которой будет изображение и ссылка
на другую страницу, на которой будет отображаться форма
для загрузки изображений."""

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/file')
def file():
    return render_template("file_form.html")

if __name__ == '__main__':
    app.run(debug=True)

