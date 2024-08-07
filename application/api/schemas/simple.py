from pydantic import BaseModel, Field


class SimpleSchema(BaseModel):
    """Simple schema 1."""

    id: int = Field(description="Id")
    name: str = Field(description="Название")
