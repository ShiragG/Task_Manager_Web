from fastapi import APIRouter

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/new')
def create_user():
    pass