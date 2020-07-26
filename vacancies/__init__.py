from flask import Flask
from flask_migrate import Migrate

from vacancies.admin import *
from vacancies.config import Config
from vacancies.models import db, Vacancy, Company, Application, Speciality, User

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
admin.init_app(app)
migrate = Migrate(app, db)


from vacancies.views import *