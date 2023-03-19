from application.extensions import db
from os import stat
from sqlalchemy import desc

class Comic(db.Model):
    __tablename__ = 'comics'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    display_name = db.Column(db.String(100))

    def json(self):
        return {'id': self.id, 'name': self.name, 'display_name': self.display_name}

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.display_name!r})"
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_comic_by_id(cls, id):
        return cls.query.filter_by(id=id).first() 

    def save(self):
        db.session.add(self)
        db.session.commit()    


