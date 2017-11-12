# @author HHN
# @Copyright https://haojie.org
from flask import Blueprint

admin_blueprint = Blueprint('admin',__name__)

from .views import EmployeeView

