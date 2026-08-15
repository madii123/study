from time import time
from fastapi import FastAPI, Request

# Pass the request to the next layer. is call_next
# middleware is a function that runs before and after each request.
# It can be used to modify the request or response, or to perform some action before or after the request is processed.
# here it is only for http requests, not websocket requests.
#
# Best practice:
# - keep middleware registration separate from app creation
# - export a setup function from this file
# - call setup_middleware(app) from main.py after app is created
# This avoids circular imports and ensures the app is fully initialized before
# middleware is attached.


def setup_middleware(app: FastAPI):
    @app.middleware("http")
    async def log_request(request: Request, call_next):
        response = await call_next(request)
        return response

    @app.middleware("http")
    async def timer(request: Request, call_next):
        start_time = time()
        response = await call_next(request)
        print(time() - start_time)
        return response
