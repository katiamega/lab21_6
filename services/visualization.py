from domain.models import db, Clients, Products, Shops
import plotly
import plotly.graph_objs as go
import json


def client_distribution_pie(uuid):
    client = db.session.query(Products.product_id.label("product_id"),
                            db.func.count(Products.product_id).label("product_idCount")).filter(
        Products.product_id == uuid).group_by(
        Products.product_id).subquery()
    data = db.session.query(db.func.sum(client.product_idCount)
                            ).group_by(client.Product_name).all()
    pie_plot = [
        go.Pie(
            labels=[value[0] for value in data],
            values=[value[1] for value in data]
        )
    ]
    return json.dumps(pie_plot, cls=plotly.utils.PlotlyJSONEncoder)

def product_shops_population_bar(name):
    data = db.session.query(Shops.Shop_name, db.func.count(Shops.shop_id)).join(
        Products, Products.product_id == Shops.product_idFk
    ).filter(Products.Product_name == name).group_by(Shops.Shop_name).all()

    bar_plot = [
        go.Bar(
                x=[value[0] for value in data],
                y=[value[1] for value in data]
        )
    ]

    return json.dumps(bar_plot, cls=plotly.utils.PlotlyJSONEncoder)
