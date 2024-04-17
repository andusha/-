from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    StringField,
    SubmitField,
    BooleanField,
    PasswordField,
    IntegerField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Email, Length, EqualTo, InputRequired
from wtforms.fields import DateField, DateTimeField


class LoginForm(FlaskForm):
    email = StringField(
        render_kw={"placeholder": "Email"},
    )
    psw = PasswordField(
        "Пароль: ",
        validators=[
            DataRequired(),
            Length(min=4, max=100, message="Пароль должен быть от 4 до 100 символов"),
        ],
        render_kw={"placeholder": "Пароль"},
    )
    submit = SubmitField("Войти")


class RegisterForm(FlaskForm):
    name = StringField(
        "ФИО: ",
        validators=[
            Length(min=4, max=100, message="Имя должно быть от 4 до 100 символов")
        ],
        render_kw={"placeholder": "ФИО"},
    )
    email = StringField(
        "Email: ",
        validators=[Email("Некорректный email")],
        render_kw={"placeholder": "Email"},
    )
    phone = StringField("Phone: ", render_kw={"placeholder": "Телефон"})
    driver_license = StringField(
        "driver_license: ",
        render_kw={"placeholder": "серия и номер водительского удостоверения"},
    )
    psw = PasswordField(
        "Пароль: ",
        validators=[
            DataRequired(),
            Length(min=4, max=100, message="Пароль должен быть от 4 до 100 символов"),
        ],
        render_kw={"placeholder": "Пароль"},
    )

    submit = SubmitField("Регистрация")


class StatementForm(FlaskForm):

    date = DateField(
        "Дата брони:",
        format="%Y-%m-%d",
        render_kw={"placeholder": "Дата брони"},
    )
    cars = SelectField(
        "Машины:",
        render_kw={"placeholder": "Машины"},
        choices=[(1, "Волга"), (2, "Жигули")],
    )

    submit = SubmitField("Оставить заявку")
