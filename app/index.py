import math

from flask import render_template, request, redirect, jsonify, session
import dao
from app import app, login
from flask_login import login_user
import utils


@app.route("/")
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')

    cates = dao.get_categories()
    prods = dao.get_products(kw, cate_id, page)

    num = dao.count_product()

    return render_template('index.html', products=prods
                           , pages=math.ceil(num / app.config['PAGE_SIZE']))


# khi nó cần lấy ối tượng user nó vô đây lấy


# chỉ chạy khi đuược gửi thông tin dang post thôi
@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    # viết câu chứng thực nếu nó thành công trả về trang home, thâ bại thì báo lỗi
    user = dao.auth_user(username=username, password=password)

    if user:
        login_user(user=user)
    return redirect('/admin')


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)


@app.route("/api/cart", methods=['post'])
def add_to_cart():
    data = request.json

    cart = session.get('cart')
    # nếu giỏ chưa có thì tạo 1 giỏ rỗng
    if cart is None:
        cart = {}

    id = str(data.get("id"))
    if id in cart:  # sản phẩm đã có trong giỏ
        cart[id]['quantity'] += 1
    else:
        cart[id] = {
            "id": id,
            "name": data.get("name"),
            "price": data.get("price"),
            "quantity": 1
        }
    session['cart'] = cart

    print(cart)

    return jsonify(utils.count_cart(cart))


@app.route('/cart')
def cart():
    return render_template('layout/cart.html')


# đổ những dữ liệu chung cho page nào cũng có
@app.context_processor
def common_response():
    return {
        'categories': dao.get_categories(),
        'cart': utils.count_cart(session.get('cart'))
    }

if __name__ == '__main__':
    from app import admin

    app.run(debug=True, port=5500)
