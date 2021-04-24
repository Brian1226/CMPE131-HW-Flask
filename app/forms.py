from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
   """
   A form that include fields for:

   'Author' (String) = enter the user's name that's writing the message
   'Message' (String) = enter the user's desired text
   Submit (button) = a submit button that says 'Send', which will send the message if clicked
   """

   # author (string) validator should make this textbox required
   author = StringField('Author', validators = [DataRequired()])

   # message (string) validator should make this textbox required
   message = StringField('Message', validators = [DataRequired()])

   # submit (button) text should say 'Send'
   submit = SubmitField('Send')
