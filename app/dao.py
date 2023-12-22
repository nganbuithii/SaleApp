from app.models import Category, Product, User

# file này để viết các phương thức
def get_categories():
    return Category.query.all()


# in ra hết


def get_products(kw):
    products = Product.query
    if kw:
        products = products.filter(Product.name.contains(kw))
    return products.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)