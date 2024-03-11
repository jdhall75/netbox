from typing import List
import strawberry
import strawberry_django
from strawberry.schema.config import StrawberryConfig

from . import models


@strawberry_django.type(
    models.DummyModel,
    fields='__all__',
)
class DummyModelType:
    pass


"""
@strawberry.type
class DummyQuery:
    @strawberry.field
    def dummymodel(self, id: int) -> DummyModelType:
        return None
    dummymodel_list: List[DummyModelType] = strawberry_django.field()

schema = strawberry.Schema(
    query=DummyQuery,
    # config=StrawberryConfig(auto_camel_case=False),
)
"""


@strawberry.type
class Query:
    fruits: list[int] = strawberry_django.field()


schema2 = strawberry.Schema(
    query=Query,
)
