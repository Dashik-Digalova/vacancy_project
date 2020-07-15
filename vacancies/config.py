import os

db_path = os.path.join("postgresql://", "postgres:postgres@127.0.0.1:5432", "vacancy")


class Config:
    DEBUG = True
    SECRET_KEY = 'my-super-secret-phrase-I-dont-tell-this-to-nobody'
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False