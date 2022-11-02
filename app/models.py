from orm.model import Model
from orm.fields import StringField, PrimaryKeyField, TextField, DecimalField, IntegerField


class Person(Model):
    __migrate__ = True
    id = PrimaryKeyField()
    first_name = StringField(max_length=40)
    last_name = StringField(max_length=40)
    email = StringField(max_length=50)
    age = IntegerField(True)


class Car(Model):
    __migrate__ = True
    id = PrimaryKeyField()
    color = StringField(max_length=40)
    model = StringField(max_length=40)
    description = TextField()
    price = DecimalField(max_digit=20, decimal_place=2)
