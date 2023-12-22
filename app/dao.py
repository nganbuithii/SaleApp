def get_categories():
    return [{
        "id": 1,
        "name": " mobile"
    }, {
        "id": 2,
        "name": " tablet"
    }]

def get_products(kw):
    products = [{
        "id":1,
        "name":"iphone 13",
        "price":20000000,
        "image":"https://i.ebayimg.com/images/g/z9MAAOSwp0Rh2~vw/s-l140.png"
    },{
        "id":2,
        "name":"galaxy s23",
        "price":15000000,
        "image":"https://i.ebayimg.com/images/g/qfUAAOSwHSdh2~vr/s-l960.png"
    },{
        "id":3,
        "name":"iphone 13",
        "price":25000000,
        "image":"https://i.ebayimg.com/images/g/U94AAOSwLiFh2~vy/s-l960.png"
    },{
        "id":4,
        "name":"iphone 13",
        "price":25000000,
        "image":"https://i.ebayimg.com/images/g/U94AAOSwLiFh2~vy/s-l960.png"
    },{
        "id":5,
        "name":"iphone 13",
        "price":25000000,
        "image":"https://i.ebayimg.com/images/g/U94AAOSwLiFh2~vy/s-l960.png"
    }]
    if kw:
        products = [p for p in products if p['name'].find(kw)>=0]
    return products