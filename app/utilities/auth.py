from werkzeug.security import check_password_hash
from models import User
from tornado import gen


@gen.coroutine
def get_user(email, password):

    users = yield User.objects.filter(email=email).find_all()

    if not users and not len(users):
        return None

    user = users[0]

    if check_password_hash(user.password, password):
        return user

    return None
