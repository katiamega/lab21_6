from wtforms import StringField, DateTimeField, IntegerField, SubmitField, validators, SelectField
from flask_wtf import FlaskForm
from domain import models
from domain.layout import city_type



class VendorsViewModel(FlaskForm):
    Vendor_name = StringField("Vendor_name: ", [validators.DataRequired("Please enter  Vendor_name.")])
    City = IntegerField("City: ",  [validators.DataRequired("Please enter  City.")])
    Rating = IntegerField("Rating: ", [validators.NumberRange(min=1, max=9),validators.DataRequired("Can be >0 and <10.")])
    Year = IntegerField("Year: ", [validators.DataRequired("Please enter  Year.")])
    Product = SelectField("Product ", validators=[validators.DataRequired()])
    CreatedOn = DateTimeField("Created On")

    Submit = SubmitField("Save")

    def domain(self):
        return models.Vendors(
            Vendor_name=self.Vendor_name.data,
            City=self.City.data,
            Rating=self.Rating.data,
			Year=self.Year.data,
			CreatedOn=self.CreatedOn.data,
            product_idIdFk=self.Product.data
        )
