from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Length, DataRequired, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('username', [InputRequired(message="Введите что-нибудь"), Length(min=2, message="Поле должно содержать минимум два символа")])
    first_name = StringField('First_name', [InputRequired(message="Введите что-нибудь"), Length(min=2, message="Поле должно содержать минимум два символа")])
    last_name = StringField('last_name', [InputRequired(message="Введите что-нибудь"), Length(min=2, message="Поле должно содержать минимум два символа")])
    password = PasswordField(
        "password",
        validators=[
            DataRequired(),
            Length(min=5, message="Пароль должен быть не менее 5 символов"),
            EqualTo('confirm_password', message="Пароли не одинаковые")
        ]
    )
    confirm_password = PasswordField("confirm_password")


class AuthForm(FlaskForm):
    username = StringField('username', [DataRequired(message="Введите что-нибудь")])
    password = PasswordField('password', [DataRequired(message="Неверный логин или пароль")])


class ApplicationForm(FlaskForm):
    written_username = StringField('written_username', [DataRequired(message="Введите что-нибудь")])
    written_phone = StringField('written_phone', [Length(min=7, message="Неверный телефон")])
    written_cover_letter = TextAreaField('written_cover_letter')


class CompanyForm(FlaskForm):
    name = StringField('Название компании', [DataRequired(message="Введите что-нибудь")])
    location = StringField('География', [DataRequired(message="Введите что-нибудь")])
    description = TextAreaField('Информация о компании')
    logo = StringField('Логотип')
    employee_count = StringField('Количество человек в компании', [DataRequired(message="Введите что-нибудь")])
