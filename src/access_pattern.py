from models.access_pattern import db, Access_pattern
from json import dumps


class Access_pattern:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def add(self):
        access_pattern = Access_pattern(
            name=self.name, description=self.description)
        db.session.add(access_pattern)
        db.session.commit()

    def get(self):
        row = db.session.execute(f'SELECT * FROM access_pattern')
        return dumps(dict(row))
