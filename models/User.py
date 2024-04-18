from .Base import Base
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
  __tablename__ = "user"

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(30))
  fullname = Mapped[Optional[str]]

  def __repr__(self) -> str:
    return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
