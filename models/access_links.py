from database.database import db


class Access_links(db.Model):
    id = db.Column('id', db.BigInteger, primary_key=True, autoincrement=True)
    link = db.Column('link', db.String)
    link_name = db.Column('link_name', db.String)
    access_apps_id = db.Column(
        'access_apps_id', db.BigInteger, db.ForeignKey('access_apps.id'))

    def __init__(self, link, link_name, access_apps_id):
        self.link = link
        self.link_name = link_name
        self.access_apps_id = access_apps_id

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "link": self.link, "link_name": self.link_name, "access_apps_id": self.access_apps_id}
        else:
            return {"col": getattr(self, col) for col in columns}
