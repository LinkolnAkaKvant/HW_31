import datetime

from dateutil.relativedelta import relativedelta
from rest_framework.exceptions import ValidationError


def check_birth_date(birth_date):
    year_diff = relativedelta(datetime.date.today(), birth_date).years
    if year_diff < 9:
        raise ValidationError(f"У пользователя возраст {year_diff} лет! Разрешено только с 9-ти лет!")


def check_email(email):
    email_list = ["mail.ru", "rambler.ru", "gmail.com", "tut.by", "yandex.ru"]
    if email is not email_list:
        raise ValidationError(f"Регистрация с этого домена запрещена!")
