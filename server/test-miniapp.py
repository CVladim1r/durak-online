from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/register")
async def register_user(user_id: int = Body(...), username: str = Body(...), first_name: str = Body(...)):
    # Здесь можно добавить логику регистрации пользователя в вашем приложении
    return {"message": f"Пользователь зарегистрирован: User ID: {user_id}, Username: {username}, First Name: {first_name}"}
