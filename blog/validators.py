from django.core.exceptions import ValidationError
import re

def username_validators(username):
    if len(username) < 5 or len(username) > 20:
        raise ValidationError("invalid username please enter a valid username") 
    if not (re.match(r'^[a-zA-Z0-9_]*[a-zA-Z]+[a-zA-Z0-9_]*$', username)):
        raise ValidationError("invalid username please enter a valid username")

def password_validators(password):
    Sum = 0
    for pas in password:
        if pas.isdigit():
            Sum += int(pas)
    if len(password) < 8 or len(password) > 50:
        raise ValidationError("invalid password please enter a valid password")
    if Sum % 6 == 0:
        raise ValidationError("invalid password please enter a valid password")
    if re.search(r"\s", password):
        raise ValidationError("invalid password please enter a valid password")
