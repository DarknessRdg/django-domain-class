class AbstractRepository(object):
    def __init__(self, model_class=None):
        self.model_class = model_class

    def create(self, *args, **kwargs):
        return self.model_class(*args, **kwargs).to_domain()

    def delete(self, domain):
        return self.model_class.from_domain(domain).delete()

    def save(self, domain):
        return self.model_class.from_domain(domain).save()

    def all(self):
        return self.filter()

    def filter(self, *args, **kwargs):
        return [
            model.to_domain()
            for model in self.model_class.objects.filter(*args, **kwargs)
        ]

    @classmethod
    def using(cls, other_class):
        return cls(model_class=other_class)
