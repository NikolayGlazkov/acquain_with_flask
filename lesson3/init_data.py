from app import app, db, Student, Fakultet

# Замените "your_flask_app_file" на имя вашего файла Flask-приложения

def initialize_data():
    # Создаем объекты моделей
    fakultet1 = Fakultet(fakult_name='Факультет1')
    fakultet2 = Fakultet(fakult_name='Факультет2')

    student1 = Student(first_name='Имя1', last_name='Фамилия1', gender='М', group='Группа1', fakultet=fakultet1)
    student2 = Student(first_name='Имя2', last_name='Фамилия2', gender='Ж', group='Группа2', fakultet=fakultet2)

    # Добавляем объекты в сессию
    db.session.add(fakultet1)
    db.session.add(fakultet2)
    db.session.add(student1)
    db.session.add(student2)

    # Коммитим изменения
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        initialize_data()
