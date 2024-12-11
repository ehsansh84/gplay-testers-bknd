import os, sys
import uvicorn
import sentry_sdk
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
project_dir = os.getenv("PROJECT_DIR")
if project_dir:
    sys.path.append(project_dir)
from app.api.v1.user import router as user_router
from app.api.v1.content import router as content_router
from app.api.v1.category import router as category_router
from app.api.v1.privacy import router as privacy_router
from app.api.v1.health_check import router as health_check_router
from app.api.v1.like import router as like_router
from app.api.v1.share import router as share_router
from app.api.v1.theme import router as theme_router
from app.api.v1.visit import router as visit_router
from app.api.v1.setting import router as setting_router
from app.api.v1.reference import router as reference_router
from app.api.v1.shop import router as shop_router
from app.api.v1.subscribe import router as subscribe_router
from app.api.v1.our_apps import router as our_apps_router

sentry_sdk.init(
    dsn="https://f8dde9c4865811efb51c0242ac12002b@sentry.pixanio.com/6",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
)

app = FastAPI(
    title="Jomlex backend",
    description="This is an API server for the app: Jomlex",
    version="1.0.0"
)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0

app.include_router(router=user_router)
app.include_router(router=content_router)
app.include_router(router=category_router)
app.include_router(router=privacy_router)
app.include_router(router=health_check_router)
app.include_router(router=like_router)
app.include_router(router=share_router)
app.include_router(router=theme_router)
app.include_router(router=visit_router)
app.include_router(router=setting_router)
app.include_router(router=reference_router)
app.include_router(router=shop_router)
app.include_router(router=subscribe_router)
app.include_router(router=our_apps_router)
app.mount("/static", StaticFiles(directory='static'), name="static")
# app.mount("/uploaded", StaticFiles(directory=Settings.UPLOAD_PATH), name="uploaded")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8200, reload=True)
