import math

from flask import render_template, request
import dao
from app import app, login


@app.route("/")
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')

    cates = dao.get_categories()
    prods = dao.get_products(kw, cate_id, page)

    num = dao.count_product()

    return render_template('index.html', categories=cates, products=prods
                           , pages=math.ceil(num/app.config['PAGE_SIZE']))


# khi nó cần lấy ối tượng user nó vô đây lấy
@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)


# chỉ chạy khi đuược gửi thông tin dang post thôi
@app.route('/admin/login', methods=['post'])
def admin_login():
    request.form.get('username')
    request.form.get('password')
    # viết câu chứng thực nếu nó thành công trả về trang home, thâ bại thì báo lỗi


if __name__ == '__main__':
    from app import admin

    app.run(debug=True, port=5500)
