import os, sys
import uvicorn
import sentry_sdk
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
project_dir = os.getenv("PROJECT_DIR")
if project_dir:
    sys.path.append(project_dir)
from app.api.v1.test_log import router as test_logrouter

sentry_sdk.init(
    dsn="https://f42ecd13ecf3fd56818667660e2c0a52@sentry.pixanio.com/9",
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

app.include_router(router=test_logrouter)
app.mount("/static", StaticFiles(directory='static'), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8200, reload=True)
