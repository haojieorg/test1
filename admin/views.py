# @author HHN
# @Copyright https://haojie.org
from flask import render_template,redirect,url_for
from flask.views import MethodView

class EmployeeView(MethodView):
    def get(self):
        return render_template('base.html')
    def post(self):
        pass