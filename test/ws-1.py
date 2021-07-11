from os import environ

import uvicorn
from fastapi import FastAPI, Query
from redis import Redis
from pydantic import RedisDsn

app = FastAPI()


@app.get("/echo")
def echo():
    return dict(environ)


@app.get('/set_redis')
def set_redis(
        url: RedisDsn = Query(...),
        key: str = Query('test_key'),
        value: str = Query('test_value')
):
    redis = Redis.from_url(url, decode_responses=True)
    try:
        redis.set(key, value)
        res = redis.get(key)
    except Exception as e:
        return f'Exc: {e.args}'
    finally:
        redis.close()
    return res


@app.get('/get_redis')
def get_redis(
        url: RedisDsn = Query(...),
        key: str = Query('test_key')
):
    redis = Redis.from_url(url, decode_responses=True)
    try:
        res = redis.get(key)
    finally:
        redis.close()
    return res


if __name__ == "__main__":
    uvicorn.run(app, debug=True, host='0.0.0.0', port=8080)
