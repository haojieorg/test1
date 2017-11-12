# @author HHN
# @Copyright https://haojie.org
from flask_wtf import Form
from wtforms import StringField,FloatField,DateField,RadioField,SelectField
from wtforms.validators import DataRequired

class EmployeeForm(Form):
    name =StringField('姓名')
    gender = RadioField('性别',choices=[('男','男'),('女','女')])
    job = StringField('职位',default='工程师')
    department = SelectField('部门')
    salary = FloatField('工资')
    birthdate = DateField('生日')
    idcard = StringField('员工编号')
    address = StringField('住址')