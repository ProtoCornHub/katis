from ..core import utils, database
from ..repositories.auth.auth_repository import oauth2_scheme
from ..schemas import user as user_schema
from ..models import user as user_model
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=user_schema.UserOut)
def create_user(user: user_schema.UserCreate, db: Session = Depends(database.get_db)):
    # hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = user_model.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/{id}', response_model=user_schema.UserOut)
def get_user(id: int, db: Session = Depends(database.get_db),
             access_token: str = Depends(oauth2_scheme)):
    user = db.query(user_model.User).filter(user_model.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user
