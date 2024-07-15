from sqlalchemy import Column, BigInteger, String

class Access_pattern_model:
  __tablename__ = "access_pattern"
  id = Column('id', BigInteger, primary_key=True, autoincrement=True)
  name = Column('name', String)
  description = Column('description', String)

  def __init__(self, name, description):
    self.name = name
    self.description = description