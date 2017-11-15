# @author HHN
# @Copyright https://haojie.org
from flask import Blueprint

admin_blueprint = Blueprint('admin',__name__)

from .views import EmployeeView,AddEmployeeView

emplistview=EmployeeView.as_view('emplist')

admin_blueprint.add_url_rule('/list/',view_func=emplistview)
admin_blueprint.add_url_rule('/list/<int:page>/',view_func=emplistview)

admin_blueprint.add_url_rule('/post/',view_func=AddEmployeeView.as_view('addemp'))