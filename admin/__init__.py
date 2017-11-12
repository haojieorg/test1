# @author HHN
# @Copyright https://haojie.org
from flask import Blueprint

admin_blueprint = Blueprint('admin',__name__)

from .views import EmployeeView

admin_blueprint.add_url_rule('/list/',view_func=EmployeeView.as_view('emplist'))