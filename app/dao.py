from app.models import Category, Product


def get_categories():
    return Category.query.all()


# in ra hết


def get_products(kw):
    products = Product.query
    if kw:
        products = products.filter(Product.name.contains(kw))
    return products.all()
