from fastapi import FastAPI, Response, Request

serverApp = FastAPI(version="0.0.0.1", description="this is just a sample serverApp i am testing")

@serverApp.get("/{item}")
def homeRoute(item: int):
    return {"status":"this serverApp is ready to go!", "number": item}

print("okay sir")