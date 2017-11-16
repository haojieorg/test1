# @author HHN
# @Copyright https://haojie.org
from flask_wtf import FlaskForm
from wtforms import StringField,FloatField,DateField,RadioField,SelectField
from wtforms.validators import DataRequired

class EmployeeForm(FlaskForm):
    name =StringField('姓名',validators=[DataRequired()])
    gender = RadioField('性别',choices=[('男','男'),('女','女')],default='男')
    job = StringField('职位',default='工程师')
    departmentid = SelectField('部门')
    salary = FloatField('工资')
    birthdate = DateField('生日')
    idcard = StringField('员工编号')
    address = StringField('住址')