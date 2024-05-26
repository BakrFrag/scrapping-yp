from fastapi import FastAPI
from api import router
from utils import setup_logging

setup_logging()
app = FastAPI()
app.include_router(router,prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)