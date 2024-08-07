from typing import List

from fastapi import APIRouter, status

from api.schemas.simple import SimpleSchema

router_simple = APIRouter(prefix="/simple1", tags=["simple1"])


@router_simple.get(
    "/",
    response_model=List[SimpleSchema],
    status_code=status.HTTP_200_OK,
)
def get_all_simple():
    """Get all items."""
    return [SimpleSchema(id=1, name="Name1"), SimpleSchema(id=2, name="Name2")]


@router_simple.get(
    "/{item_id}",
    response_model=SimpleSchema,
    status_code=status.HTTP_200_OK,
)
def get_one_simple(simple_id: int):
    """Get one item."""
    return SimpleSchema(id=simple_id, name=f"Name{simple_id}")
