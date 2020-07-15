from flask import Flask

from vacancies.config import Config
from vacancies.models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


from vacancies.views import *