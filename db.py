from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database:
  def __init__(self, db_file, Base):
    global engine, Session
    engine = create_engine(f"sqlite:///{db_file}", connect_args={'check_same_thread': False})
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)