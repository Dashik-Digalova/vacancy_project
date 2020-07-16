from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from vacancies.models import *

admin = Admin()

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Vacancy, db.session))
admin.add_view(ModelView(Speciality, db.session))
admin.add_view(ModelView(Company, db.session))
admin.add_view(ModelView(Application, db.session))



