from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from vacancies.config import Config
from vacancies.data import *
from vacancies.static import *

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Vacancy(db.Model):
    __tablename__ = "vacancies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    speciality = db.relationship("Speciality", back_populates="vacancies")
    company = db.relationship("Company", back_populates="vacancies")
    skills = db.Column(db.String)
    description = db.Column(db.String, nullable=False)
    salary_min = db.Column(db.String)
    salary_max = db.Column(db.String)
    published_at = db.Column(db.DateTime, nullable=False)
    speciality_code = db.Column(db.String, db.ForeignKey("specialities.code"))
    company_name = db.Column(db.String, db.ForeignKey("companies.name"))


class Company(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    location = db.Column(db.String)
    logo = db.Column(db.String)
    description = db.Column(db.String)
    employee_count = db.Column(db.String)
    vacancies = db.relationship("Vacancy", back_populates="company")


class Speciality(db.Model):
    __tablename__ = "specialities"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False, unique=True)
    title = db.Column(db.String, nullable=False)
    picture = db.Column(db.String, nullable=False)
    vacancies = db.relationship("Vacancy", back_populates="speciality")


#db.create_all()


#for vacancy in jobs:
#    vacancies = Vacancy(title=vacancy["title"], description=vacancy["desc"], salary_min=vacancy["salary_from"], salary_max=vacancy["salary_to"],
#                        published_at = vacancy["posted"], speciality_code=vacancy["cat"], company_name=vacancy["company"])
#    db.session.add(vacancies)

#for c in companies:
#    company=Company(name=c["title"])
#    db.session.add(company)

#for s in specialties:
#    spec = Speciality(code=s["code"], title=s["title"], picture="/static/check.png")
#    db.session.add(spec)





db.session.commit()








