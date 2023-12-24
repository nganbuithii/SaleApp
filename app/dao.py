import hashlib

from app.models import Category, Product, User
from app import app


# file này để viết các phương thức
def get_categories():
    return Category.query.all()


# in ra hết


def get_products(kw, cate_id, page=None):
    products = Product.query
    if kw:
        products = products.filter(Product.name.contains(kw))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    # phân trang
    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']

        start = (page - 1) * page_size
        end = start + page_size

        return products.slice(start, end)

    return products.all()


# đếm số lượng sản phẩm có trên database
def count_product():
    return Product.query.count()


def get_user_by_id(user_id):
    return User.query.get(user_id)


# chứng thực tài khoản
def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()
