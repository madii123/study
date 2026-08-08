from fastapi import APIRouter, HTTPException
import httpx


router = APIRouter()


@router.get("/fun")
async def fun():
    async with httpx.AsyncClient() as client:
        #response = await client.get("https://example.com")
        response = await client.post("https://example.com", data={"key": "value"})
        if response.status_code != 200:

            raise HTTPException(
                status_code=404,
                detail="user not found"
            )
    return response.json()
