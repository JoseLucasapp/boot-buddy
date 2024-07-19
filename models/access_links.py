from database.database import db
from json import dumps
from sqlalchemy import text


class Access_links(db.Model):
    __tablename__ = 'access_links'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link = db.Column('link', db.String)
    link_name = db.Column('link_name', db.String)
    access_apps_id = db.Column(
        'access_apps_id', db.Integer, db.ForeignKey('access_apps.id'))

    def __init__(self, link, link_name, access_apps_id):
        self.link = link
        self.link_name = link_name
        self.access_apps_id = access_apps_id

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "link": self.link, "link_name": self.link_name, "access_apps_id": self.access_apps_id}
        else:
            return {"col": getattr(self, col) for col in columns}

    def add(self):
        access_links = Access_links(
            link=self.link, link_name=self.link_name, access_apps_id=self.access_apps_id)
        db.session.add(access_links)
        db.session.commit()

    def get(self):
        result = db.session.execute(
            text('SELECT * FROM access_links')).fetchall()
        return dumps([dict(row._mapping) for row in result])
