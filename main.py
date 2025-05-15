from fastapi import FastAPI, HTTPException
from pydantic import ValidationError

from app.api.dependencies import setup_dependencies
from app.api.routes import setup_routers


def create_app() -> FastAPI:
    app = FastAPI(
        title="Ualá test social network",
        description="Microblogging platform similar to Twitter",
        version="0.1.0",
    )

    setup_dependencies(app)

    setup_routers(app)

    return app


app = create_app()
