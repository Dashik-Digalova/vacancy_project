from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


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
    speciality_code = db.Column(db.Integer, db.ForeignKey("specialities.id"))
    company_name = db.Column(db.Integer, db.ForeignKey("companies.id"))
    applications = db.relationship("Application", back_populates="vacancy")


class Company(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    location = db.Column(db.String)
    logo = db.Column(db.String)
    description = db.Column(db.String)
    employee_count = db.Column(db.String)
    vacancies = db.relationship("Vacancy", back_populates="company")
    owner = db.relationship("User", back_populates="companies")
    owner_companies = db.Column(db.Integer, db.ForeignKey("users.id"))


class Speciality(db.Model):
    __tablename__ = "specialities"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False, unique=True)
    title = db.Column(db.String, nullable=False)
    picture = db.Column(db.String)
    vacancies = db.relationship("Vacancy", back_populates="speciality")


class Application(db.Model):
    __tablename__ = "applications"
    id = db.Column(db.Integer, primary_key=True)
    written_username = db.Column(db.String, nullable=False)
    written_phone = db.Column(db.String, nullable=False)
    written_cover_letter = db.Column(db.Text, nullable=False)
    vacancy = db.relationship("Vacancy", back_populates="applications")
    user = db.relationship("User", back_populates="applications")
    vacancy_app = db.Column(db.Integer, db.ForeignKey("vacancies.id"))


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)
    companies = db.relationship("Company", back_populates="owner")
    applications = db.relationship("Application", back_populates="user")
    user_app = db.Column(db.Integer, db.ForeignKey("applications.id"))

    @hybrid_property
    def password_hash(self):
        # Запретим прямое обращение к паролю
        raise AttributeError("Вам не нужно знать пароль!")

    @password_hash.setter
    def password_hash(self, password):
        # Устанавливаем пароль через этот метод
        self._password_hash = generate_password_hash(password)

    def password_valid(self, password):
        # Проверяем пароль через этот метод
        # Функция check_password_hash превращает password в хеш и сравнивает с хранимым
#        print(self._password_hash, password)
        return check_password_hash(self._password_hash, password)



#db.create_all()


#for vacancy in jobs:
#    vacancies = Vacancy(title=vacancy["title"], description=vacancy["desc"], salary_min=vacancy["salary_from"],
#                        salary_max=vacancy["salary_to"], published_at = vacancy["posted"],
#                        speciality_code=vacancy["cat"], company_name=vacancy["company"])
#    db.session.add(vacancies)

#for c in companies:
#    company=Company(name=c["title"])
#    db.session.add(company)

#for s in specialties:
#    spec = Speciality(code=s["code"], title=s["title"], picture="/static/check.png")
#    db.session.add(spec)


#db.session.commit()








