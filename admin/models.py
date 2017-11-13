# @author HHN
# @Copyright https://haojie.org
from run import db


class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)

    def __init__(self,name):
        self.name = name


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
    department = db.relationship('Department',backref=db.backref('employees',lazy='dynamic'))

    def __init__(self,name,gender,job,salary,birthdate,idcard,address):
        self.name = name
        self.gender = gender
        self.job = job
        self.salary = salary
        self.birthdate = birthdate
        self.idcard = idcard
        self.address = address




