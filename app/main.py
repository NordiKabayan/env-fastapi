from fastapi import FastAPI
import redis

app = FastAPI()
r = redis.Redis(host="redis", port=6379)

@app.get("/")
def read_root():
    return {"Hello": "NordiKabayan.gg"}

@app.get("/count")
def read_root():
    r.incr("index")
    return { "Hit Count": r.get("index") }