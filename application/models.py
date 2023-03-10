from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass

class Comic(Base):
    __tablename__ = 'comics'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    display_name: Mapped[Optional[str]] = mapped_column(String(100))
    # display_source = StringCol()
    # date_publish = DateCol()
    # title = StringCol(notNone=True)
    # alt = StringCol()
    # perm_link = StringCol(notNone=True)
    # img_url = StringCol()
    # prev_link = StringCol()
    # prev_id = IntCol()
    # next_link = StringCol()
    # next_id = IntCol()
    # img_file = StringCol()

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.display_name!r})"
    
engine = create_engine('mysql://root:mariarootp@localhost/sarjis', echo=True)

Base.metadata.create_all(engine)


