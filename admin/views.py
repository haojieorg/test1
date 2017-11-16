# @author HHN
# @Copyright https://haojie.org
from flask import render_template,redirect,url_for,request
from flask.views import MethodView
from admin.forms import EmployeeForm
from admin.models import db
from admin.models import Department
from admin.models import Employee


class EmployeeView(MethodView):

    def get(self,page=None):
        from admin.models import Employee
        emp = Employee.query.paginate(page,per_page=20)
        return render_template('emplist.html',emp=emp)

    def post(self):
        pass

class AddEmployeeView(MethodView):

    def get(self,id=None):
        emp = Employee() if not id else Employee.query.get(id)
        form = EmployeeForm(request.form,obj=emp)
        form.departmentid.choices=[(d.id,d.name) for d in Department.query.all()]
        return render_template('addemp.html',form=form)

    def post(self,id=None):

        form = EmployeeForm(request.form)
        emp = Employee() if not id else Employee.query.get(id)
        form.populate_obj(emp)
        if not id:
            db.session.add(emp)
        db.session.commit()
        return redirect(url_for('admin.emplist'))

class EmployeeDeleteView(MethodView):
    def get(self,id=None):
        emp = Employee.query.get(id)
        db.session.delete(emp)
        db.session.commit()
        return redirect(url_for('admin.emplist'))

