from wtforms import StringField, DateTimeField, IntegerField, SubmitField, SelectField, validators
from flask_wtf import FlaskForm
from domain import models



class TestsViewModel(FlaskForm):
	Price = IntegerField("Price: ", [validators.DataRequired("Please enter Price.")])
	Productor = StringField("Productor: ", [validators.DataRequired("Please enter Productor.")])
	Client = SelectField("Client", validators=[validators.DataRequired()])
	CreatedOn = DateTimeField("Created On")

	Submit = SubmitField("Save")

	def domain(self):
		return models.Tests(
			Price=self.Price.data,
			Productor=self.Productor.data,
			CreatedOn=self.CreatedOn.data,
			client_idIdFk=self.Client.data
		)