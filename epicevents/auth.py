from functools import wraps


def is_logged_in():
    ...  # déterminer si l'utilisateur est connecté
    return False  # retourner True si l'utilisateur et connecté et False sinon


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_logged_in():
            return print(
                "Connectez-vous préalablement à l'aide de la commande "
                "$python -m epiecevents login"
            )
        return func(*args, **kwargs)

    return wrapper
