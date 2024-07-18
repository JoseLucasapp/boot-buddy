from database.database import db
from json import dumps
from sqlalchemy import text


class Access_pattern(db.Model):
    __tablename__ = 'access_pattern'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String)
    description = db.Column('description', db.String)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "name": self.name, "description": self.description}
        else:
            return {"col": getattr(self, col) for col in columns}

    def add(self):
        access_pattern = Access_pattern(
            name=self.name, description=self.description)
        db.session.add(access_pattern)
        db.session.commit()

    def get(self):
        result = db.session.execute(
            text('SELECT * FROM access_pattern')).fetchall()
        return dumps([dict(row._mapping) for row in result])
