from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models import Category, Product, UserRoleEnum
from flask_login import login_user, current_user
from flask import redirect


# MUỐN TẠO 1 PAGE K DÍNH TỚI MODEL TH IMPORT BASEVIEW và expose
admin = Admin(app=app, name=" QUẢN TRỊ BÁN HÀNG", template_mode='bootstrap4')


class AuthenticatedAdmin(ModelView):
    # chỉ định người truy cập - khoog cho vào
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN

class MyProductView(AuthenticatedAdmin):
    column_list = ['id', 'name', 'price']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['price']
    column_editable_list = ['name', 'price']

    # chỉ định người truy cập - khoog cho vào
    # dễ bị lặp code nên  viết 1 class cho 2 lớp kế thừa
    # def is_accessible(self):
    #     return current_user.is_authenticated

class MyCategoryView(AuthenticatedAdmin):
    column_list = ['name', 'products']


class StatsView(BaseView):
    @expose("/")
    def __index__(self):
        return self.render('admin/stats.html')


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))

admin.add_view(StatsView(name="THỐNG KÊ BÁO CÁO"))
