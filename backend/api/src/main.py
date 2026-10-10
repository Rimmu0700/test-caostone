from fastapi import FastAPI

from src.modules.health import controller as health_controller


def create_app() -> FastAPI:
    application = FastAPI(title="Usada Bali API", version="1.1.0")
    application.include_router(health_controller.router)
    return application


app = create_app()
