from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView
from flask_login import current_user, LoginManager
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink

from app import app, db
from app.models import OwnerModel, PetModel, UserModel


class OwnerModelViews(ModelView):
    form_excluded_columns = 'pets'


class UserModelViews(ModelView):
    def is_accessible(self):
        return current_user.admin


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))


admin = Admin(app, index_view=MyAdminIndexView())
login = LoginManager(app)


@login.user_loader
def load_user(user_id):
    return UserModel.query.get(user_id)


admin.add_view(UserModelViews(UserModel, db.session, 'User'))
admin.add_view(OwnerModelViews(OwnerModel, db.session, 'Owner'))
admin.add_view(ModelView(PetModel, db.session, 'Pet'))
admin.add_link(MenuLink('Logout', '/logout'))
