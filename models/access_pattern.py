from database.database import db
from sqlalchemy import text


class Access_pattern(db.Model):
    __tablename__ = 'access_pattern'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column('name', db.String)
    description = db.Column('description', db.String)

    def add(name, description):
        access_pattern = Access_pattern(
            name=name,
            description=description)

        db.session.add(access_pattern)
        db.session.commit()
        return access_pattern

    def get():
        result = db.session.execute(
            text('SELECT * FROM access_pattern')).fetchall()
        return [dict(row._mapping) for row in result]
