from typing import List

from fastapi import APIRouter, status

from api.simple1.schemas import Simple1Schema

router_simple1 = APIRouter(prefix="/simple1", tags=["simple1"])


@router_simple1.get(
    "/",
    response_model=List[Simple1Schema],
    status_code=status.HTTP_200_OK,
)
def get_all_simple1():
    return [
        Simple1Schema(id=1, name="Name1"),
        Simple1Schema(id=2, name="Name2"),
    ]


@router_simple1.get(
    "/{item_id}",
    response_model=Simple1Schema,
    status_code=status.HTTP_200_OK,
)
def get_one_simple2(simple_id: int):
    return Simple1Schema(id=simple_id, name=f"Name{simple_id}")
