import time

import structlog
from fastapi import Request

from core.settings import settings

logger = structlog.get_logger()


async def log_requests(request: Request, call_next):
    if not settings.LOG_ENABLED:
        return await call_next(request)

    start_time = time.time()

    logger.info(
        "http_request_start",
        method=request.method,
        path=request.url.path,
    )

    response = await call_next(request)

    duration = time.time() - start_time

    logger.info(
        "http_request_end",
        method=request.method,
        path=request.url.path,
        status_code=response.status_code,
        duration_ms=int(duration * 1000),
    )

    return response
