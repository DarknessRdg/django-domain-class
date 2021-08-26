import app.models
from app.repositories.abstract import AbstractRepository


class UserRepository(AbstractRepository):
    """
    Repositório com todas as queries utilizadas pelo domain de Model.
    É de extra importancia que todos os argumentos dos métodos seja apenas
    de alto nível e que não tenham relação com a estrutura do model.

    Um exemplo é a query de filtro por nome `with_name`.
    Ela recebe o nome a ser filtrado, e a sua impelemntação é quem faz o
    filter utilizando o campo correto do model.

    Caso haja a necessidade de fazer uma chamada para um model diferente,
    pode-se utiliazr o método `using()` de `AbstractRepository`.
    Um exemplo desse caso é o método `exists_on_old_database()` que verifica
    se o usuario existe na base de dados antiga utilizando o model `LegacyUser`
    """
    def __init__(self):
        super().__init__(model_class=app.models.User)

    def active(self):
        return self.filter(active=True, deleted__isnull=True)

    def without_password(self):
        return self.filter(password__isnull=True)

    def with_name(self, name: str):
        return self.filter(name=name)

    def exists_on_old_database(self, domain):
        return self.using(app.models.LegacyUser).filter(domain.to_model())
