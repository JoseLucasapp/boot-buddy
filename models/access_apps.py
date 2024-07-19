from database.database import db
from json import dumps
from sqlalchemy import text


class Access_apps(db.Model):
    __tablename__ = 'access_apps'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column('name', db.String)
    path = db.Column('path', db.String)
    is_browser = db.Column('is_browser', db.Integer)

    access_patterns_id = db.Column(
        'access_patterns_id',
        db.Integer,
        db.ForeignKey('access_pattern.id'))

    def __init__(self, name, access_patterns_id, path, is_browser):
        self.name = name
        self.access_patterns_id = access_patterns_id
        self.path = path
        self.is_browser = is_browser

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id,
                    "name": self.name,
                    "path": self.path,
                    "access_patterns_id": self.access_patterns_id,
                    "is_browser": self.is_browser}
        else:
            return {"col": getattr(self, col) for col in columns}

    def add(self):
        print(self)
        access_app = Access_apps(
            name=self.name,
            access_patterns_id=self.access_patterns_id,
            path=self.path,
            is_browser=self.is_browser)

        db.session.add(access_app)
        db.session.commit()
        return access_app

    def get(self):
        result = db.session.execute(
            text('SELECT * FROM access_apps')).fetchall()
        return dumps([dict(row._mapping) for row in result])
