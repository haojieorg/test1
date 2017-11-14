# @author HHN
# @Copyright https://haojie.org
from flask import render_template,redirect,url_for,request
from flask.views import MethodView
from admin.forms import EmployeeForm
from admin.models import db
class EmployeeView(MethodView):

    def get(self):
        from admin.models import Employee
        emp = Employee.query.order_by(db.desc(Employee.id)).limit(20)
        return render_template('emplist.html',emp=emp)

    def post(self):
        pass

class AddEmployeeView(MethodView):

    def get(self):
        from admin.models import Department
        form = EmployeeForm()
        form.departmentid.choices=[(d.id,d.name) for d in Department.query.all()]
        return render_template('addemp.html',form=form)

    def post(self):
        from admin.models import Employee
        form = EmployeeForm(request.form)
        emp = Employee(
            form.name.data,
            form.gender.data,
            form.job.data,
            form.salary.data,
            form.birthdate.data,
            form.idcard.data,
            form.address.data,
        )
        emp.departmentid=int(form.departmentid.data)
        db.session.add(emp)
        db.session.commit()
        return redirect(url_for('admin.emplist'))

