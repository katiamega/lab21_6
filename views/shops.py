from wtforms import StringField, DateTimeField, IntegerField, SubmitField, validators, SelectField
from flask_wtf import FlaskForm
from domain import models



class ShopsViewModel(FlaskForm):
    Shop_name = StringField("Shop_name: ", [validators.DataRequired("Please enter  Shop_name.")])
    Locale = StringField("Locale: ", [validators.DataRequired("Please enter Locale.")])
    Shop_contact = IntegerField("Shop_contact: ", [validators.DataRequired("Please enter Shop_contact.")])
    Product = SelectField("Product ", validators=[validators.DataRequired()])
    CreatedOn = DateTimeField("Created On")

    Submit = SubmitField("Save")

    def domain(self):
        return models.Shops(
            Shop_name=self.Shop_name.data,
            Locale=self.Locale.data,
            Shop_contact=self.Shop_contact.data,
			CreatedOn=self.CreatedOn.data,
            product_idIdFk=self.Product.data
        )
