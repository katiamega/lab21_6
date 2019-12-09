from wtforms import StringField, DateTimeField, IntegerField, SubmitField, validators
from flask_wtf import FlaskForm
from domain import models



class ClientsViewModel(FlaskForm):

    Client_name = StringField("Client_name: ", [validators.DataRequired("Please enter your Name.")])
    Age = IntegerField("Age: ", [validators.DataRequired("Please enter your Age.")])
    Money = IntegerField("Money: ", [validators.DataRequired("Please enter your Money.")])
    Contact = IntegerField("Contact: ", [validators.DataRequired("Please enter your Contact.")])
    CreatedOn = DateTimeField("Created On")

    Submit = SubmitField("Save")

    def domain(self):
        return models.Clients(
            Client_name=self.Client_name.data,
            Age=self.Age.data,
            Money=self.Money.data,
            Contact=self.Contact.data,
            CreatedOn=self.CreatedOn.data
        )