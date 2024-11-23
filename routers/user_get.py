from enum import Enum

from fastapi import APIRouter, status


router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_user(id: int,):
    '''
    Возвращает пользователя
    '''
    return {'user': id}
