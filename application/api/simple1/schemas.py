from pydantic import (
    BaseModel,
    Field
)


class Simple1Schema(BaseModel):
    id: int = Field(description="Id")
    name: str = Field(description="Название")
