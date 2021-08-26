from app.repositories.user import UserRepository


class User(object):
    def __new__(cls, *args, **kwargs):
        # cria a cria o atributo `objects` aqui para evitar
        # dependencia ciclica
        cls.objects = UserRepository()

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
