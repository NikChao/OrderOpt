from peewee import (Model, TextField, BooleanField, DateTimeField, IntegerField, FloatField,
                    ForeignKeyField)

from webapi.database import database

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    class Meta:
        db_table = 'users'

    id = IntegerField()
    user_name = TextField()
    password_hash = TextField()

