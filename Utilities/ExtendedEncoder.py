from django.forms import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model


class ExtendedEncoder(DjangoJSONEncoder):
    """To extend the Django JSON Encoder and return a dict
        containing the data in the instance of the Model.

    Keyword arguments:
    o -- object of the Django Model
    Return: a dict containing the data of the object
    """

    def default(self, o):
        if isinstance(o, Model):
            return model_to_dict(o)

        return super().default(o)