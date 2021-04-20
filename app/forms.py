from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    """
    A form that include fields for:

    'author' (String) = enter the name of the person writing the message
    'message' (String) = enter the desired text
    submit (button) = a submit button that says 'Send'

    """

    # author (string) validator should make this textbox required
    author = StringField('Author', validators = [DataRequired()])

    # message (string) validator should make this textbox required
    message = StringField('Message', validators = [DataRequired()])

    # submit (button) text should say 'Send'
    submit = SubmitField('Send')
