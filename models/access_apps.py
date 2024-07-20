from database.database import db
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

    def add(name, access_patterns_id, path, is_browser):
        access_app = Access_apps(
            name=name,
            access_patterns_id=access_patterns_id,
            path=path,
            is_browser=is_browser)

        db.session.add(access_app)
        db.session.commit()
        return access_app

    def get():
        result = db.session.execute(
            text('SELECT * FROM access_apps')).fetchall()
        return [dict(row._mapping) for row in result]

    def get_by_pattern_id(pattern_id):
        result = db.session.execute(text(
            f"SELECT * FROM access_apps WHERE access_patterns_id = '{pattern_id}'")).fetchall()

        return [dict(row._mapping) for row in result]
