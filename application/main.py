from typing import List

from fastapi import FastAPI, APIRouter

from api import all_routers


def create_routers(main_app: FastAPI, routers: List[APIRouter]) -> None:
    """Create routers."""
    for router in routers:
        main_app.include_router(router)


app = FastAPI()
create_routers(app, all_routers)
