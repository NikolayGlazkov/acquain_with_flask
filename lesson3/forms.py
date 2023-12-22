from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,IntegerField,EmailField,SubmitField
from wtforms.validators import DataRequired,Email, EqualTo,Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    conferm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign In')



# class RegisterForm(FlaskForm):
#     name = SelectField('Name',validators=[DataRequired()])
#     age = IntegerField("Age",validators=[DataRequired()])
#     gender = SelectField('Gender',choices=[("male","Мужчина")('female',"Женьщина")])


# class RegistrationForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])