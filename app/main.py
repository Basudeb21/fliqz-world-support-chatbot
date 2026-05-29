from fastapi import FastAPI

from app.api.routes.chat import router as chat_router


app = FastAPI(
    title="Fliqz AI Support"
)

app.include_router(chat_router)


@app.get("/")
async def root():

    return {
        "message": "Fliqz AI Support Running"
    }