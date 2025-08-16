from fastapi import FastAPI, Response, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from random import choice

serverApp = FastAPI(version="0.0.0.1", description="this is just a sample serverApp i am testing")

@serverApp.middleware("http")
async def userAgent(req: Request, call_next):
    if req.headers.get("jwt") == "1234":
        response = await call_next(req)
        return response
    else:
        return JSONResponse(
            status_code=401,
            content={"status": "error", "response": "Sorry we couldn't verify your identity"}
        )

class responseModel(BaseModel):
    status: str
    response: str

class requestModel(BaseModel):
    query: str

@serverApp.post("/poster", response_model=responseModel, status_code=200)
def posterHander(payLoad: requestModel):
    greetings = [
        f"Hello, Mr {payLoad.query}. It's nice to meet you!",  
        f"Hi there, Mr {payLoad.query}! Great to meet you.",
        f"Good day, Mr {payLoad.query}! Pleasure to meet you.",
        f"Hey, Mr {payLoad.query}! How's it going?",
        f"Greetings, Mr {payLoad.query}! Nice to see you.",
        f"Hello, Mr {payLoad.query}! I've been looking forward to meeting you.",
        f"Hi, Mr {payLoad.query}! Hope you're doing well.",
        f"Salutations, Mr {payLoad.query}! Nice to make your acquaintance.",
        f"Hey there, Mr {payLoad.query}! Pleasure to meet you.",
        f"Good to see you, Mr {payLoad.query}! How are you!"
    ]
    greet = choice(greetings)
    return {"status": "success", "response": greet}

@serverApp.get("/{item}")
def homeRoute(item: str):
    return {"status": "this serverApp is ready to go!", "number": item}