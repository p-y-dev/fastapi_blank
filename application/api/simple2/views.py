from fastapi import (
    APIRouter,
    status
)
from api.simple2.schemas import Simple2Schema
from typing import List

router_simple2 = APIRouter(prefix="/simple2", tags=["simple2"])


@router_simple2.get(
    "/",
    response_model=List[Simple2Schema],
    status_code=status.HTTP_200_OK,
)
def get_all_simple1():
    return [
        Simple2Schema(id=1, name='Name1'),
        Simple2Schema(id=2, name='Name2'),
    ]


@router_simple2.get(
    "/{item_id}",
    response_model=Simple2Schema,
    status_code=status.HTTP_200_OK,
)
def get_one_simple2(simple_id: int):
    return Simple2Schema(id=simple_id, name=f'Name{simple_id}')
