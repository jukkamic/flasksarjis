from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

class Comic():
    __tablename__ = 'comics'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    display_name = Column(String(100))

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
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    


