from app.repositories.abstract import AbstractRepository
from app.repositories.user import UserRepository


class AbstractDomain(object):
    objects: AbstractRepository

    def save(self):
        self.objects.save(self)

    def delete(self):
        self.objects.delete(self)


class User(AbstractDomain):
    def __new__(cls, *args, **kwargs):
        # cria a cria o atributo `objects` aqui para evitar
        # dependencia ciclica
        cls.objects = UserRepository()

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
