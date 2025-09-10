from fastapi import FastAPI
from langserve import add_routes
from chatbot import chatbot_runnable
import uvicorn

app = FastAPI(
    title="Fast Chatbot API",
    version="1.0.0"
)

# Add LangServe route
add_routes(
    app,
    chatbot_runnable,
    path="/chatbot"
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
