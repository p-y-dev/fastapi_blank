from fastapi import FastAPI
from api import all_routers


def create_routers(main_app: FastAPI, routers: tuple):
    for router in routers:
        main_app.include_router(router)


app = FastAPI()
create_routers(app, all_routers)
