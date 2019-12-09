from flask import Flask, request, render_template, redirect, url_for
from domain.models import db, Clients, Tests, Products, Shops, Vendors, Inits
from domain.credentials import *
from views.clients import ClientsViewModel
from views.tests import TestsViewModel
from views.products import ProductsViewModel
from views.shops import ShopsViewModel
from views.vendors import VendorsViewModel
from views.inits import InitsViewModel

from sqlalchemy import desc
import os

app = Flask(__name__)
app.secret_key = 'development key'

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL",
                                                  f"postgresql://{username}:{password}@{hostname}:{port}/{database}")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def index():
    db.create_all()
    return render_template("layout.html")

@app.route('/map')
def map():
    db.create_all()
    client_1=Clients(client_name='Kat',client_age='30',client_money='2000',client_contact='07846351')
    test_1=Tests(price='1500', productor='Uk', client_idIDFK='1')
    product_1=Products(product_name='cafe',product_price='1200',test_idIDFK='1')
    shop_1=Shops(shop_name='romantic',locale='Kyiv',shop_contact='044123567', product_idIDFK='1')
    vendor_1=Vendors(vendor_name='Katia',city='Kyiv', rating='8',year='2018',product_idIdFk='1')
    db.session.add_all([client_1,test_1,product_1,shop_1,vendor_1])
    db.session.commit()
    return render_template("layout.html")

@app.route('/get')
def get():
    clients=Clients.query.all()
    tests=Tests.query.all()
    products=Products.query.all()
    shops=Shops.query.all()
    vendors=Vendors.query.all()
    return render_template("layout.html",clients=clients,tests=tests,products=products,shops=shops,vendors=vendors)



@app.route("/clients")
def clients():
    all_clients = Clients.query.all()
    return render_template("clients/index.html", clients=all_clients)


@app.route("/clients/new", methods=["GET", "POST"])
def new_client():
    form = ClientsViewModel()

    if request.method == "POST":
        if not form.validate():
            return render_template("clients/create.html", form=form)
        else:
            client = form.domain()
            clients = Clients.query.filter_by().all()
            ids = [client_data.client_id for client_data in clients]
            ids.append(0)
            client.client_id = max(ids) + 1
            db.session.add(client)
            db.session.commit()
            return redirect(url_for("clients"))

    return render_template("clients/create.html", form=form)


@app.route("/clients/delete/<uuid>", methods=["POST"])
def delete_client(uuid):
    client = Clients.query.filter(Clients.client_id == uuid).first()
    if client:
        db.session.delete(client)
        db.session.commit()

    return redirect(url_for("clients"))


@app.route("/clients/<uuid>", methods=["GET", "POST"])
def update_client(uuid):
    client = Clients.query.filter(Clients.client_id == uuid).first()
    form = client.wtf()

    if request.method == "POST":
        if not form.validate():
            return render_template("clients/update.html", form=form)

        client.map_from(form)
        db.session.commit()
        return redirect(url_for("clients"))

    return render_template("clients/update.html", form=form)


@app.route("/tests")
def tests():
    all_tests = Tests.query.join(Clients).order_by(desc(Tests.CreatedOn)).all()
    return render_template("tests/index.html", tests=all_tests)


@app.route("/tests/new", methods=["GET", "POST"])
def new_test():
    form = TestsViewModel()
    form.Client.choices = [(str(client.client_id), client.Client_name) for client in Clients.query.all()]

    if request.method == "POST":
        if not form.validate():
            return render_template("tests/create.html", form=form)
        else:
            client = form.domain()
            tests = Tests.query.filter_by().all()
            ids = [test_data.test_id for test_data in tests]
            ids.append(0)
            client.test_id = max(ids) + 1
            db.session.add(client)
            db.session.commit()
            return redirect(url_for("tests"))

    return render_template("tests/create.html", form=form)


@app.route("/tests/delete/<uuid>", methods=["POST"])
def delete_test(uuid):
    test = Tests.query.filter(Tests.test_id == uuid).first()
    if test:
        db.session.delete(test)
        db.session.commit()

    return redirect(url_for("tests"))


@app.route("/tests/<uuid>", methods=["GET", "POST"])
def update_test(uuid):
    test = Tests.query.filter(Tests.test_id == uuid).first()
    form = test.wtf()
    form.Client.choices = [(str(client.client_id), client.Client_name) for client in Clients.query.all()]

    if request.method == "POST":
        if not form.validate():
            return render_template("tests/update.html", form=form)
        test.map_from(form)
        db.session.commit()
        return redirect(url_for("tests"))

    return render_template("tests/update.html", form=form)


@app.route("/products")
def products():
    all_products = Products.query.join(Tests).order_by(desc(Products.CreatedOn)).all()
    return render_template("products/index.html", products=all_products)


@app.route("/products/new", methods=["GET", "POST"])
def new_product():
    form = ProductsViewModel()
    form.Test.choices = [(str(test.test_id), test.Price) for test
                         in Tests.query.join(Clients, Tests.client_idIdFk == Clients.client_id).all()]

    if request.method == "POST":
        if not form.validate():
            return render_template("products/create.html", form=form)
        else:
            client = form.domain()
            products = Products.query.filter_by().all()
            ids = [product_data.product_id for product_data in products]
            ids.append(0)
            client.product_id = max(ids) + 1
            db.session.add(client)
            db.session.commit()
            return redirect(url_for("products"))

    return render_template("products/create.html", form=form)


@app.route("/products/<uuid>", methods=["GET", "POST"])
def update_product(uuid):
    product = Products.query.filter(Products.product_id == uuid).first()
    form = product.wtf()
    form.Test.choices = [(str(test.test_id), test.Price) for test
                         in Tests.query.join(Clients, Tests.client_idIdFk == Clients.client_id).all()]

    if request.method == "POST":
        if not form.validate():
            return render_template("products/update.html", form=form)
        product.map_from(form)
        db.session.commit()
        return redirect(url_for("products"))

    return render_template("products/update.html", form=form)


@app.route("/products/delete/<uuid>", methods=["POST"])
def delete_product(uuid):
    product = Products.query.filter(Products.product_id == uuid).first()
    if product:
        db.session.delete(product)
        db.session.commit()

    return redirect(url_for("products"))


@app.route("/shops")
def shops():
    all_shops = Shops.query.join(Products).all()
    return render_template("shops/index.html", shops=all_shops)


@app.route("/shops/new", methods=["GET", "POST"])
def new_shop():
    form = ShopsViewModel()
    form.Product.choices = [(str(product.product_id), product.Product_name) for product
                            in Products.query.join(Tests, Products.test_idIdFk == Tests.test_id).all()]

    if request.method == "POST":
        if not form.validate():
            return render_template("shops/create.html", form=form)
        else:
            test = form.domain()
            shops = Shops.query.filter_by().all()
            ids = [shop_data.shop_id for shop_data in shops]
            ids.append(0)
            test.shop_id = max(ids) + 1
            db.session.add(test)
            db.session.commit()
            return redirect(url_for("shops"))

    return render_template("shops/create.html", form=form)


@app.route("/shops/<uuid>", methods=["GET", "POST"])
def update_shop(uuid):
    shop = Shops.query.filter(Shops.shop_id == uuid).first()
    form = shop.wtf()
    form.Product.choices = [(str(product.product_id), product.Product_name) for product
                            in Products.query.join(Tests, Products.test_idIdFk == Tests.test_id).all()]

    if request.method == "POST":
        if not form.validate():
            return render_template("shops/update.html", form=form)
        shop.map_from(form)
        db.session.commit()
        return redirect(url_for("shops"))

    return render_template("shops/update.html", form=form)


@app.route("/shops/delete/<uuid>", methods=["POST"])
def delete_shop(uuid):
    shop = Shops.query.filter(Shops.shop_id == uuid).first()
    if shop:
        db.session.delete(shop)
        db.session.commit()

    return redirect(url_for("shops"))
	
	
@app.route("/workers")
def workers():
    all_workers = Workers.query.join(Shops).all()
    return render_template("workers/index.html", workers=all_workers)


@app.route("/workers/new", methods=["GET", "POST"])
def new_worker():
    form = WorkersViewModel()
    form.Shop.choices = [(str(shop.shop_id), shop.Shop_name) for shop
                            in Shops.query.join(Products, Shops.product_idIdFk == Products.product_id).all()]

    if request.method == "POST":
        if not form.validate():
            return render_template("workers/create.html", form=form)
        else:
            product = form.domain()
            workers = Workers.query.filter_by().all()
            ids = [worker_data.worker_id for worker_data in workers]
            ids.append(0)
            product.worker_id = max(ids) + 1
            db.session.add(product)
            db.session.commit()
            return redirect(url_for("workers"))

    return render_template("workers/create.html", form=form)


@app.route("/workers/<uuid>", methods=["GET", "POST"])
def update_worker(uuid):
    worker = Workers.query.filter(Workers.worker_id == uuid).first()
    form = worker.wtf()
    form.Shop.choices = [(str(shop.shop_id), shop.Shop_name) for shop
                            in Shops.query.join(Products, Shops.product_idIdFk == Products.product_id).all()]

    if request.method == "POST":
        if not form.validate():
            return render_template("workers/update.html", form=form)
        worker.map_from(form)
        db.session.commit()
        return redirect(url_for("workers"))

    return render_template("workers/update.html", form=form)


@app.route("/workers/delete/<uuid>", methods=["POST"])
def delete_worker(uuid):
    worker = Workers.query.filter(Workers.worker_id == uuid).first()
    if worker:
        db.session.delete(worker)
        db.session.commit()

    return redirect(url_for("workers"))
	
	
	
	
if __name__ == "__main__":
    app.run(debug=True)
