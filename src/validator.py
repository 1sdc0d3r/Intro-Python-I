import re


def validate_email(email):
    if len(email) > 7:
        return bool(re.match("[a-zA-Z]!@$%^&*()_+.=-{1,3}|", email))
