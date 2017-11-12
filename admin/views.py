# @author HHN
# @Copyright https://haojie.org
from flask import render_template,redirect,url_for
from flask.views import MethodView

class EmployeeView(MethodView):
    def get(self):
        from admin.models import Employee
        emp = Employee.query.limit(20)
        return render_template('emplist.html',emp=emp)
    def post(self):
        pass