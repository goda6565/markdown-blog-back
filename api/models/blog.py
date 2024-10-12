from datetime import date
from typing import Optional
from sqlmodel import Field, SQLModel

class Blog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    text: str
    created_at: date = Field(
        nullable=False,
        default_factory=lambda: date.today(),
    )
    updated_at: date = Field(
        nullable=False,
        default_factory=lambda: date.today(),
    )