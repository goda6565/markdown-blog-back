from typing import List
from fastapi import APIRouter, Depends, HTTPException

import schemas.blog as blog_schema
import cruds.blog as blog_crud
from sqlmodel import Session
from db import get_session

router = APIRouter()


@router.get("/blogs", response_model=List[blog_schema.Blog])
async def read_blogs(session: Session = Depends(get_session)):
    return await blog_crud.read_Blogs(session)



@router.post("/blogs", response_model=blog_schema.BlogCreateResponse)
async def create_blog(blog_body: blog_schema.BlogCreate, session: Session = Depends(get_session)):
    return await blog_crud.create_Blog(session, blog_body)


@router.get("/blogs/{blog_id}", response_model=blog_schema.Blog)
async def read_blog(blog_id: int, session: Session = Depends(get_session)):
    return await blog_crud.read_Blog(session, id=blog_id)


@router.patch("/blogs/{blog_id}", response_model=blog_schema.BlogCreateResponse)
async def update_blog(blog_id: int, blog_body: blog_schema.BlogCreate, session: Session = Depends(get_session)):
    blog = await blog_crud.read_Blog(session, id=blog_id)
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return await blog_crud.update_Blog(session, blog_body, original=blog)


@router.delete("/blogs/{blog_id}", response_model=None)
async def delete_blog(blog_id: int, session: Session = Depends(get_session)):
    blog = await blog_crud.read_Blog(session, id=blog_id)
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return await blog_crud.delete_Blog(session, original=blog)