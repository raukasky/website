from fastapi import APIRouter

from app.core import settings

router = APIRouter()


@router.get('/info',
            description='Website info', )
def get_info():
    return {
        "website name": settings.PROJECT_NAME,
        "environment": settings.ENVIRONMENT
    }


@router.get('/check')
def get_health():
    return {
        "status": "OK"
    }