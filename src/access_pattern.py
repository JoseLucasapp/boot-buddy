from models.access_pattern import db, Access_pattern_model


class Access_pattern:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def add(self):
        access_pattern = Access_pattern_model(
            name=self.name, description=self.description)
        db.session.add(access_pattern)
        db.session.commit()
