# @author HHN
# @Copyright https://haojie.org
from run import db


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    job = db.Column(db.String)
    salary = db.Column(db.Float)
    birthdate = db.Column(db.Date)
    idcard = db.Column(db.String)
    address = db.Column(db.String)

    departmentid = db.Column(db.Integer,db.ForeignKey('department.id'))
    department = db.relationship('Department',backref=db.backref('employees'))



class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)

    def __init__(self,name):
        self.name = name
