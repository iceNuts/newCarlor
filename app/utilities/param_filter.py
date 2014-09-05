import re

def is_email(email):

    allowed_email_suffix = [
        'wustl.edu',
    ]

    if re.match(r'[^@]+@[^@]+\.[^@]+', email):
        suffix = email.split('@')[1]

        if suffix in allowed_email_suffix:
            return True

    return False


def is_ObjectID(object_id):

    if re.match(r'[0-9a-zA-Z]{24}', object_id):

        return True

    return False

def is_phone(phone_number):

    if re.match(r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$', phone_number):

        return True

    return False