import locale

from flask import abort, render_template, request, redirect, session

from vacancies import app
from vacancies.forms import *
from vacancies.models import *

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
    vacancies = list(db.session.query(Vacancy).filter(Vacancy.company_name == company.name))
    if company is None:
        abort(404)
    return render_template("company.html", company=company, vacancies=vacancies)


@app.route("/vacancies/<int:vacancy_id>/")
def render_vacancy_page(vacancy_id):
    form = ApplicationForm()

    vacancy = Vacancy.query.get(vacancy_id)
    company = Company.query.all()
    company_data = []
    for i in company:
        if i.name == vacancy.company_name:
            company_data.append(i)
    if vacancy is None:
        abort(404)
    return render_template("vacancy.html", vacancy=vacancy, company_data=company_data, form=form)


@app.route("/vacancies/<int:vacancy_id>/send")
def send_request(vacancy_id):
    return render_template("sent.html")


@app.route("/mycompany/")
def render_company():
    render_template("company-edit.html")


@app.route("/mycompany/vacancies/")
def show_company_vacancies():
    return render_template("vacancy-list.html")


@app.route("/mycompany/vacancies/<int:vacancy_id>/")
def show_my_vacancy(vacancy_id):
    return render_template("vacancy-edit.html")


@app.route("/login/", methods=["GET", "POST"])
def render_login():
    if session.get("user_id"):
        return redirect("/")
    form = AuthForm()
    if request.method == "POST":
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        if user and user.password_valid(form.password.data):
            session["user_id"] = {
                "id": user.id,
                "username": user.username,
            }
            return redirect("/")

    return render_template("login.html", form=form)


@app.route("/register/", methods=["GET", "POST"])
def render_register():
    form = RegisterForm()
    if request.method == "POST" and form.validate_on_submit():
        username = form.username.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        password_hash = form.password.data
        user = User(username=username, first_name=first_name, last_name=last_name)
        user.password_hash = password_hash
        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            error_msg = 'Такой пользователь существует'
            return render_template("register.html", error_msg=error_msg, form=form)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("register.html", form=form)


@app.route("/logout/")
def render_logout():
    if session.get("user_id"):
        session.pop("user_id")
    return redirect("/")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.template_filter("words_ending")
def words_ending(value, s="вакансия, вакансии, вакансий"):
    number = abs(int(value))
    s = s.split(",")
    if number % 10 == 1 and number % 100 != 11:
        return s[0]
    elif number % 10 == 2 and number % 100 != 12 or number % 10 == 3 and number % 100 != 13 or number % 10 == 4 \
            and number % 100 != 14:
        return s[1]
    else:
        return s[2]



