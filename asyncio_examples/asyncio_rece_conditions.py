from fastapi import FastAPI, HTTPException
import asyncio
from random import randint

app = FastAPI()

inscriptions_db = {"total_slots": 1000000, "reserved_slots": 0}

slots_lock = asyncio.Lock()

async def process_checkout(user_id: str):

    await asyncio.sleep(randint(1, 3) / 1000)

    async with slots_lock:
        if inscriptions_db["reserved_slots"] >= inscriptions_db["total_slots"]:
            raise HTTPException(status_code=400, detail="No slots available")
        
        inscriptions_db["reserved_slots"] += 1
        return {"message": "Successfully registered", "user_id": user_id, "slot_number": inscriptions_db["reserved_slots"]}

@app.post("/register/{user_id}")
async def register(user_id: str):
    return await process_checkout(user_id)

@app.get("/status")
async def status():
    return inscriptions_db
