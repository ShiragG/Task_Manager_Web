from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix='/user',
    tags=['user']
)

class UserModel(BaseModel):
    login: str
    password: str
    email: str
    role_id: int
    first_name: str
    second_name: str
    last_name: str | None
    user_position: str


@router.post('/new')
def create_user(user: UserModel):
    return 'ok'