from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField

class ProductForm(FlaskForm):
    name = StringField('name')
    quantity = IntegerField('quantity')
    unit = StringField('unit')
    unit_price = DecimalField('unit_price')