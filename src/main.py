from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.core import config
from src.core.events import create_start_app_handler, create_stop_app_handler
from src.core.routes import service_routes, api_routes
from src.core.logging import init_logger
from fastapi_utils.timing import add_timing_middleware
from loguru import logger

def create_app():
    app = FastAPI(title=config.PROJECT_NAME, debug=config.DEBUG, version=config.VERSION, docs_url=None, redoc_url=None)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    add_timing_middleware(app, record=logger.info, prefix="solr", exclude="untimed")

    app.add_event_handler("startup", create_start_app_handler())
    app.add_event_handler("shutdown", create_stop_app_handler())

    # router
    app.include_router(service_routes, prefix=config.PAGE_PREFIX)
    # app.include_router(api_routes, prefix=config.API_PREFIX)
    app.include_router(api_routes)
    
    init_logger()

    from src.scheduler import customized_jobs
    customized_jobs.add_a_job()

    return app

app = create_app()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host="0.0.0.0", port=8000, log_level="debug")
    # gunicorn -b 127.0.0.1: 8001 -k uvicorn.workers.UvicornWorker main: api
