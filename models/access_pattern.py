from database.database import db


class Access_pattern(db.Model):
    id = db.Column('id', db.BigInteger, primary_key=True, autoincrement=True)
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
