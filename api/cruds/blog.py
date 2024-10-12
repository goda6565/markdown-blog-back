import db as model
from typing import List
import schemas.blog as blog_schema
from sqlmodel import Session, select
from datetime import date
from sqlalchemy import desc

async def create_Blog(
    session: Session, blog_create: blog_schema.BlogCreate
) -> model.Blog:
    blog = model.Blog(**blog_create.dict())
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog

async def read_Blogs(
    session: Session
) -> List[model.Blog]:
    blogs = session.exec(select(model.Blog).order_by(desc(model.Blog.id))).all()
    return blogs

async def read_Blog(
    session: Session, id: int
) -> model.Blog:
    blog = session.exec(select(model.Blog).filter(model.Blog.id == id)).first()
    return blog

async def update_Blog(
    session: Session, blog_create: blog_schema.BlogCreate, original: model.Blog
) -> model.Blog:
    original.title = blog_create.title
    original.text = blog_create.text
    original.updated_at = date.today()
    session.add(original)
    session.commit()
    session.refresh(original)
    return original

async def delete_Blog(
    session: Session, original: model.Blog
) -> None:
    session.delete(original)
    session.commit()