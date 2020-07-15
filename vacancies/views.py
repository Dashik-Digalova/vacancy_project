import locale

from flask import abort, render_template

from vacancies.models import *
from vacancies.forms import *

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


@app.route("/")
def render_main():
    categories = list(db.session.query(Speciality).order_by(db.func.random()).limit(3))
    vacancies = db.session.query(Vacancy).all()
    companies = db.session.query(Company).all()
    specialities = db.session.query(Speciality).all()
    vacancies_number = []
    company_vacancies = []
    for vacancy in vacancies:
        for speciality in specialities:
            if vacancy.speciality_code == speciality.code:
                vacancies_number.append(speciality.title)
        for company in companies:
            if vacancy.company_name == company.name:
                company_vacancies.append(company.name)
    return render_template("index.html", for_search=categories, specialities=specialities, vacancies=vacancies_number,
                           companies=companies, company_vacancies=company_vacancies)


@app.route("/vacancies/")
def show_all_vacancies():
    vacancies = db.session.query(Vacancy).all()
    return render_template("vacancies.html", vacancies=vacancies)


@app.route("/vacancies/cat/<code>/")
def show_vacancies(code):
    vacancies = db.session.query(Vacancy).filter(Vacancy.speciality_code == code)
    specialities = db.session.query(Speciality).all()
    speciality_vacancies = []
    for spec in specialities:
        if code in spec.code:
            speciality = spec.title
    for vacancy in vacancies:
        if vacancy.speciality_code == code:
            speciality_vacancies.append(vacancy)
    return render_template("vacancies.html", speciality_vacancies=speciality_vacancies, speciality=speciality)


@app.route("/companies/<int:company_id>/")
def render_company_card(company_id):
    company = Company.query.get(company_id)
    if company is None:
        abort(404)
    return render_template("company.html", company=company)


@app.route("/vacancies/<int:vacancy_id>/")
def render_vacancy_page(vacancy_id):
    vacancy = Vacancy.query.get(vacancy_id)
    company = Company.query.all()
    company_data = []
    for i in company:
        if i.name == vacancy.company_name:
            company_data.append(i)
    if vacancy is None:
        abort(404)
    return render_template("vacancy.html", vacancy=vacancy, company_data=company_data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.template_filter("words_ending")
def words_ending(value, s="вакансия, вакансии, вакансий"):
    number = abs(int(value))
    s = s.split(",")
    if number % 10 == 1 and number % 100 != 11:
        return s[0]
    elif number % 10 == 2 and number % 100 != 12 or number % 10 == 3 and number % 100 != 13 or number % 10 == 4 and number % 100 != 14:
        return s[1]
    else:
        return s[2]



