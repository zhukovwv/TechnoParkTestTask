from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.calc import router as calc_router
from api.health import router as health_router
from core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    lifespan=lifespan,
)

app.include_router(calc_router)
app.include_router(health_router)
