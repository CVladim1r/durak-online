from motor.motor_asyncio import AsyncIOMotorClient
from app.schemas import TransactionCreate, TransactionResponse
from app.models import Transaction

async def create_transaction(transaction: TransactionCreate, db: AsyncIOMotorClient):
    transaction_dict = transaction.dict()
    await db["transactions"].insert_one(transaction_dict)
    return transaction_dict

async def get_transaction_by_id(transaction_id: str, db: AsyncIOMotorClient):
    return await db["transactions"].find_one({"_id": transaction_id})
