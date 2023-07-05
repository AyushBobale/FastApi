from fastapi import APIRouter

router = APIRouter(
    prefix="/books"
)


@router.get("/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/{id}")
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.delete("/{id}")
async def read_user(username: str):
    return {"username": username}


@router.post("/{id}")
async def read_user_1(username: str):
    return {"username": username}


@router.patch("/{id}")
async def read_user_2(username: str):
    return {"username": username}
