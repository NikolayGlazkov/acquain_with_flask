"""Создать базу данных для хранения информации о студентах университета.
База данных должна содержать две таблицы: "Студенты" и "Факультеты".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
возраст, пол, группа и id факультета.
В таблице "Факультеты" должны быть следующие поля: id и название
факультета.
Необходимо создать связь между таблицами "Студенты" и "Факультеты".
Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их факультета."""
from random import choice  
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from models import Student, Faculties, db
import pandas as pd
genders = ["m", "f"]
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db.init_app(app)


# создание базы данных для хранения информации о студентах универсетета
@app.cli.command("create_db")
def create_db():
    db.create_all()
    print("Создана база данных")


# добавление студентов в базу данных
@app.cli.command("fill-db")
def fill_tanles():
    count = 20
    for user in range(1, count + 1):
        new_user = Student(
            first_name=f"user{user}",
            surname=f"my_mail{user}@mail.ru",
            age=f"{1 + user}",
            gender=choice(genders),
            group=f"{user}",
            fakult_id=1 
        )
        db.session.add(new_user)
    db.session.commit()
    # дбавляем факультеты в базу данных

    # for fakult in range(1, count**2):
       
    # db.session.commit()
    # print("ol user whos update to db")
@app.route("/")
def index():
    students = Student.query.all()
    # my_list = []
    # for student in students:
    #     my_list.append(student)

    # return render_template("index.html")
    content = pd.DataFrame(students).to_html()
    return render_template("index.html", table=content)

if __name__ == "__main__":
    app.run(debug=True)
