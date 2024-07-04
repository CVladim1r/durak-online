from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from app.schemas import TransactionCreate, TransactionResponse
from app.db import get_database
from app.services.transaction import create_transaction, get_transaction_by_id

router = APIRouter()

@router.post('/', response_model=TransactionResponse)
async def create_new_transaction(transaction: TransactionCreate, db: AsyncIOMotorClient = Depends(get_database)):
    return await create_transaction(transaction, db)

@router.get('/{transaction_id}', response_model=TransactionResponse)
async def get_transaction(transaction_id: str, db: AsyncIOMotorClient = Depends(get_database)):
    transaction = await get_transaction_by_id(transaction_id, db)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction
