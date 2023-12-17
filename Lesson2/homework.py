"""Задание

Создать страницу, на которой будет форма для ввода имени и электронной почты, 
при отправке которой будет создан cookie-файл с данными пользователя, 
а также будет произведено перенаправление на страницу приветствия, где будет 
отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти», при нажатии 
на которую будет удалён cookie-файл с
данными пользователя и произведено
перенаправление на страницу ввода имени и электронной почты."""
from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')


@app.route('/welcome', methods=['POST'])
def welcome():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        # Создание cookie с данными пользователя
        response = make_response(redirect('/greet'))
        response.set_cookie('username', name)
        response.set_cookie('email', email)
        
        return response

@app.route('/greet')
def greet():
    # Получение данных пользователя из cookie
    username = request.cookies.get('username')
    email = request.cookies.get('email')
    
    return f'Привет, {username}! Электронная почта: {email}. <a href="/logout">Выйти</a>'

@app.route('/logout')
def logout():
    # Удаление cookie и перенаправление на страницу ввода данных
    response = make_response(redirect('/'))
    response.delete_cookie('username')
    response.delete_cookie('email')
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
