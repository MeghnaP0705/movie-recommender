from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agents.movie_agent import movie_agent

app = FastAPI()

# Allow frontend at http://localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(req: Request):
    body = await req.json()
    user_id = body.get("user_id")
    message = body.get("message")
    response = movie_agent(user_id, message)
    return {"reply": response}
