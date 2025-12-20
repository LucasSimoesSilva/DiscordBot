from util import db_session

def initialize_db() -> None:
  db_session.Base.metadata.create_all(bind=db_session.engine)
  print("Database initialized.")