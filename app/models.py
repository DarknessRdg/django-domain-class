from abc import abstractmethod
from django.db import models
import app.domain


class AbstractModel(models.Model):
    """
    Clase de model abstrata com os métodos necessários para seerm implementados
    """

    @classmethod
    @abstractmethod
    def from_domain(cls, domain):
        """
        Este médoto deve retonar uma instancia do model a partir de uma
        instancia da class de dominio
        """

    @abstractmethod
    def to_domain(self):
        """
        Este método deve retrona uma instancia do dominio a partir da isntencia
        de model (self)
        """


class User(AbstractModel):
    complete_name = models.CharField(max_length=255)

    @classmethod
    def from_domain(cls, domain):
        return cls(complete_name=domain.name)

    def to_domain(self):
        return app.domain.User(id=self.id, name=self.complete_name)


class LegacyUser(AbstractModel):
    full_name = models.CharField(max_length=255)

    @classmethod
    def from_domain(cls, domain):
        return cls(id=domain.id, full_name=domain.name)

    def to_domain(self):
        return app.domain.User(id=self.id, name=self.full_name)
