from fastapi import APIRouter

dummy_router = APIRouter()


@dummy_router.get("/dummy")
def get_dummy():
    return {"hello": "bye"}
