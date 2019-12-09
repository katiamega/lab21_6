from wtforms import DateTimeField, SubmitField, validators, SelectField
from flask_wtf import FlaskForm
from domain import models


class InitsViewModel(FlaskForm):
    Product = SelectField("product", validators=[validators.DataRequired()])
    Vendor = SelectField("vendor", validators=[validators.DataRequired()])
    CreatedOn = DateTimeField("Created On")

    Submit = SubmitField("Save")

    def domain(self):
        return models.Inits(
            vendor_idIdFk=self.Vendor.data,
            product_idIdFk=self.Product.data,
            CreatedOn=self.CreatedOn.data
        )