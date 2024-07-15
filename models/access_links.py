from sqlalchemy import Column, BigInteger, String, ForeignKey

class Access_links_model:
  __tablename__ = "access_links"
  id = Column('id', BigInteger, primary_key=True, autoincrement=True)
  link = Column('link', String)
  link_name = Column('link_name', String)
  access_apps_id = Column('access_apps_id', BigInteger, ForeignKey('access_apps.id'))

  def __init__(self, link, link_name, access_apps_id):
    self.link = link
    self.link_name = link_name
    self.access_apps_id = access_apps_id