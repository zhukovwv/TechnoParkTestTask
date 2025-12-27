from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.middleware import log_requests
from core.logging import setup_logging

from api.calc import router as calc_router
from api.health import router as health_router
from core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    lifespan=lifespan,
)

# middleware
app.middleware("http")(log_requests)

# routers
app.include_router(calc_router)
app.include_router(health_router)
