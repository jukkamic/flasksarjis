from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class JsonModel(object):
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Comic(db.Model, JsonModel):
    comic_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    display_name = db.Column(db.String(100), nullable=False)
    display_source = db.Column(db.String(100))
    #date_publish = db.Columnt(db.models.DateField(_(""), auto_now=False, auto_now_add=False))
    title = db.Column(db.String())
    alt = db.Column(db.String())
    perm_link = db.Column(db.String(), nullable=False)
    img_url = db.Column(db.String())
    prev_link = db.Column(db.String())
    prev_id = db.Column(db.Integer())
    next_link = db.Column(db.String())
    next_id = db.Column(db.Integer())
    img_file = db.Column(db.String())

    def __init__(self, name, display_name, display_source, 
                 title, alt, perm_link, img_url, prev_link, prev_id, next_link, next_id, img_file):
        self.name = name
        self.display_name = display_name
        self.display_source = display_source
        #self.date_publish = date_publish
        self.title = title
        self.alt = alt
        self.perm_link = perm_link
        self.img_url = img_url
        self.prev_link = prev_link
        self.prev_id = prev_id
        self.next_link = next_link
        self.next_id = next_id
        self.img_file = img_file
        db.create_all()
