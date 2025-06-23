from typing import Generic, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

# --- Definir un tipo genérico para el contenido de 'data' ---
# T representa cualquier BaseModel que queramos poner dentro de 'data'
Model = TypeVar('Model', bound=BaseModel)


class ResponseData(GenericModel, Generic[Model]):
    data: Model | None
