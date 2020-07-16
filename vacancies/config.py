import os

db_path = os.path.join("postgresql://", "postgres:postgres@127.0.0.1:5432", "vacancy")


class Config:
    DEBUG = True
    SECRET_KEY = 'my-super-secret-phrase-I-dont-tell-this-to-nobody'
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MEDIA_URL = '/media/'
    MEDIA_ROOT = 'media'
    MEDIA_COMPANY_IMAGE_DIR = 'company_images'
    MEDIA_SPECIALITY_IMAGE_DIR = 'speciality_images'
