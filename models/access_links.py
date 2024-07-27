from database.database import db
from sqlalchemy import text


class Access_links(db.Model):
    __tablename__ = 'access_links'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    link = db.Column('link', db.String)
    link_name = db.Column('link_name', db.String)

    access_apps_id = db.Column(
        'access_apps_id',
        db.Integer,
        db.ForeignKey('access_apps.id'))

    def add(link, link_name, access_apps_id):
        access_links = Access_links(
            link=link,
            link_name=link_name,
            access_apps_id=access_apps_id)

        db.session.add(access_links)
        db.session.commit()

    def get():
        result = db.session.execute(
            text('SELECT * FROM access_links')).fetchall()
        return [dict(row._mapping) for row in result]

    def get_by_app_id(app_id):
        result = db.session.execute(text(
            f"SELECT * FROM access_links WHERE access_apps_id = '{app_id}'")).fetchall()

        return [dict(row._mapping) for row in result]

    def delete_links_by_app(app_id):
        db.session.execute(text(
            f"DELETE FROM access_links WHERE access_apps_id = '{app_id}'"
        ))
        db.session.commit()
