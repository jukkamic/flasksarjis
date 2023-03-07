from sqlobject import SQLObject, StringCol, IntCol, DateCol, sqlhub, connectionForURI

sqlhub.processConnection = connectionForURI('sqlite:///sarjis.db')

class Comic(SQLObject):
    comic_id = IntCol(unique=True)
    name = StringCol(notNone=True)
    display_name = StringCol(notNone=True)
    display_source = StringCol()
    date_publish = DateCol()
    title = StringCol(notNone=True)
    alt = StringCol()
    perm_link = StringCol(notNone=True)
    img_url = StringCol()
    prev_link = StringCol()
    prev_id = IntCol()
    next_link = StringCol()
    next_id = IntCol()
    img_file = StringCol()

    def __init__(self, name, display_name, display_source, date_publish,
                 title, alt, perm_link, img_url, prev_link, prev_id, next_link, next_id, img_file):
        self.name = name
        self.display_name = display_name
        self.display_source = display_source
        self.date_publish = date_publish
        self.title = title
        self.alt = alt
        self.perm_link = perm_link
        self.img_url = img_url
        self.prev_link = prev_link
        self.prev_id = prev_id
        self.next_link = next_link
        self.next_id = next_id
        self.img_file = img_file

Comic.createTable()
