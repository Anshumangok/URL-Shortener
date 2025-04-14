from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis
import shortuuid

app = FastAPI()

# Connect to Redis
r = redis.Redis(host='redis', port=6379, decode_responses=True)

class URLRequest(BaseModel):
    long_url: str
    custom_id: str | None = None

@app.post("/shorten")
def shorten_url(url: URLRequest):
    short_id = url.custom_id or shortuuid.ShortUUID().random(length=7)
    if r.exists(short_id):
        raise HTTPException(status_code=400, detail="Custom ID already exists")
    r.set(short_id, url.long_url)
    return {
        "short_url": f"http://localhost:8000/{short_id}",
        "long_url": url.long_url
    }

@app.get("/{short_id}")
def redirect_url(short_id: str):
    long_url = r.get(short_id)
    if not long_url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return {"long_url": long_url}

