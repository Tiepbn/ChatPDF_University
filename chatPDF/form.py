# from flask_wtf import FlaskForm
# from wtforms import StringFiled
# from chatPDF.models import User

# class RegisterForm(FlaskForm):
#     def validate_username(self, username_to_check):
#         user = User.query.filter_by(username=username_to_check.data).first();
#         if user:
#             raise ValidationError('Username already exists! Pleases try a different username')
#     def validate_email_address(self, email_address_to_check):
#         email_address = User.query.filter_by(email_address=email_address_to_check.data).first();
#         if email_address:
#             raise ValidationError('Email address already exists! Pleases try a different email address')
#     username = StringField(label='username', validators=[Length(min=2, max=30), DataRequired()])
#     email_address = StringField(label='email_address', validators=[Email(), DataRequired()])
#     password1 = PasswordField(label='password1', validators=[Length(min=6), DataRequired()])
#     password2 = PasswordField(label='password2', validators=[EqualTo('password1'), DataRequired()])
#     submit = SubmitField(label='Create Account')


# class LoginForm(FlaskForm):
#     email_address = StringField(label='email_address: ', validators=[DataRequired()])
#     password = StringField(label='Password: ', validators=[ DataRequired()])
#     submit = SubmitField(label='Sign in')