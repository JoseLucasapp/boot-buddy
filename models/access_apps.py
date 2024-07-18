from database.database import db


class Access_apps_model(db.Model):
    id = db.Column('id', db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String)
    description = db.Column('description', db.String)
    access_patterns_id = db.Column(
        'access_patterns_id', db.BigInteger, db.ForeignKey('access_patterns.id'))

    def __init__(self, name, description, access_patterns_id):
        self.name = name
        self.description = description
        self.access_patterns_id = access_patterns_id

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "name": self.name, "description": self.description, "access_patterns_id": self.access_patterns_id}
        else:
            return {"col": getattr(self, col) for col in columns}
