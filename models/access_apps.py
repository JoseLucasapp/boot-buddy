from sqlalchemy import Column, BigInteger, String, ForeignKey

class Access_apps_model:
  __tablename__ = "access_apps"
  id = Column('id', BigInteger, primary_key=True, autoincrement=True)
  name = Column('name', String)
  description = Column('description', String)
  access_patterns_id = Column('access_patterns_id', BigInteger, ForeignKey('access_patterns.id'))

  def __init__(self, name, description, access_patterns_id):
    self.name = name
    self.description = description
    self.access_patterns_id = access_patterns_id