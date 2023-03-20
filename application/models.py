from application.extensions import db
from os import stat
from sqlalchemy import desc
import logging
import json
from types import SimpleNamespace

class NotFoundException(Exception):
    pass

class Comic(db.Model):

    __tablename__ = 'comics'

    id = db.Column(db.Integer, primary_key=True)
    next_id = db.Column(db.Integer)
    name = db.Column(db.String(), nullable=False)
    display_name = db.Column(db.String())
    prev_link = db.Column(db.String())
    perm_link = db.Column(db.String())
    next_link = db.Column(db.String())
    img_url = db.Column(db.String())
    img_file = db.Column(db.String())

    def __init__(self, comic_json):
        super().__init__()
        for key in comic_json.keys():
            # if key == 'id':
            #     self.id = comic_json[key]
            # if key == 'next_id':
            #     self.next_id = comic_json[key]
            if key == 'name':
                self.name = comic_json[key]
            if key == 'display_name':
                self.display_name = comic_json[key]
            if key == 'prev_link':
                self.prev_link = comic_json[key]
            if key == 'perm_link':
                self.perm_link = comic_json[key]
            if key == 'next_link':
                self.next_link = comic_json[key]
            if key == 'img_url':
                self.img_url = comic_json[key]
            if key == 'img_file':
                self.img_file = comic_json[key]
                
        # self = json.loads(json.dumps(comic_json))
        # logging.debug("Initialized from json: %s", self)
        # if comic_json['id'] is not None:
        #     self.id = comic_json['id']
        # logging.debug("json dot next_id: %s", comic_json.next_id)
        # self.next_id = comic_json['next_id']
        # self.name = comic_json['name']
        # self.display_name = comic_json['display_name']
        # self.perm_link = comic_json['perm_link']
        # self.prev_link = comic_json['prev_link']
        # self.next_link = comic_json['next_link']

    def json(self):
        return {
            'id': self.id, 
            'next_id': self.next_id,
            'name': self.name, 
            'display_name': self.display_name, 
            'perm_link': self.perm_link, 
            'prev_link': self.prev_link,
            'next_link': self.next_link, 
            'img_url': self.img_url,
            'img_file': self.img_file,
        }

    def __repr__(self) -> str:
        return f"Comic(id={self.id!r}, next_id={self.next_id!r}, name={self.name!r}, display_name={self.display_name!r})"
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_comic_by_id(cls, id):
        logging.debug("get_comic_by_id {}".format(id))
        return cls.query.filter_by(id=id).first() 
    
    @classmethod
    def get_comic_by_permalink(cls, prev_link):

        result = cls.query.filter_by(perm_link = prev_link).first()
        if (result == None):
            raise NotFoundException("Not found. prev_link: " + prev_link)
        return result
    
    def save(self):
        logging.debug("save {} with id {}".format(self.name, self.id))
        db.session.add(self)
        db.session.commit()    
