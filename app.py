from fastapi import FastAPI, Form
from pydantic import BaseModel, Field

app = FastAPI()


class LoginFormModel(BaseModel):
    username: str
    password: str = Field(min_length=8, title='Пароль', description='Длина минимум 8 символов')


@app.post('/login/', response_model=LoginFormModel)
async def get_login_form(login_form: LoginFormModel):
    print(login_form)
    return login_form
