from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import *
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from miniFig_app import app
from miniFig_app import User
from miniFig_app import Figure
from miniFig_app import Sell_fig

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class PostSellFigForm(FlaskForm):
    # image = FileField('Upload Image', validators=[FileRequired()])
    
    fig_id= StringField('Minifig ID', validators=[DataRequired()])
    fig_name = StringField('Minifig Name', validators=[DataRequired()])
    # fig_theme = StringField('Minifig Theme', validators=[DataRequired()])
    # fig_year = SelectField(
    #     "Minifig Year",
    #     [DataRequired()],
    #     choices=list(range(2021, 1974, -1)),
    # )
    fig_quantity = IntegerField('Minifig Quantities', validators=[DataRequired()])
    fig_price = DecimalField('Set Your Price', validators=[DataRequired()])
    submit = SubmitField('Post to Sell')

    def validate_fig_id(self, fig_id):
        fig = Figure.query.filter_by(id=fig_id.data).first()
        if not fig:
            raise ValidationError('Minifigure Id is not exist, please check and input again!')
    

    def validate_fig_quantity(self, fig_quantity):
        if fig_quantity.data <= 0 :
            raise ValidationError('Quantity must be greater than 0')

    
    def validate_fig_price(self, fig_price):
        if fig_price.data<= 0:
            raise ValidationError('Price must be greater than 0')

class UserUpdateForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email', validators=[DataRequired(), Email()])
    # password = PasswordField('Password', validators=[DataRequired()])
    # password2 = PasswordField(
    #     'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Update')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class SellItemUpdateForm(FlaskForm):
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    sell_price = DecimalField('Price', validators=[DataRequired()])
    submit = SubmitField('Update')

    def validate_quantity(self, quantity):
        if quantity.data <= 0 :
            raise ValidationError('Quantity must be greater than 0')

    
    def validate_sell_price(self, sell_price):
        if sell_price.data<= 0:
            raise ValidationError('Price must be greater than 0')

class AddToCartForm(FlaskForm):
    fig_quantity = IntegerField('Purchase Quantity', validators=[DataRequired()])
    sell_fig_id = HiddenField('Sell Fig Id. this is a hidden field', 
        validators = [validators.DataRequired()])
    submit = SubmitField('Add to cart')

    def validate_quantity(self, fig_quantity, sell_fig_id):
        quantity = Sell_fig.query.filter(Sell_fig.id == sell_fig_id.data).first()
        if fig_quantity.data > quantity.quantity: #quantity???
            raise ValidationError('Purchase Quantity must less than Inventory Quantity')