from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..controllers import resources as controller
from ..schemas import resources as schema

router = APIRouter(
    prefix="/resources",
    tags=["Resources"]
)


@router.post("/", response_model=schema.Resource)
def create_resource(request: schema.ResourceCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Resource])
def get_all_resources(db: Session = Depends(get_db)):
    return controller.read_all(db=db)


@router.get("/{item_id}", response_model=schema.Resource)
def get_resource(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Resource)
def update_resource(item_id: int, request: schema.ResourceUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, item_id=item_id, request=request)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_resource(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
