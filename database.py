   
from sqlalchemy import create_engine, text
import os
db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
  connect_args={
  "ssl": {
    "ssl_ca": "C:/Users/user/Desktop/new-flask/isrgrootx1.pem"
  }
})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_dicts = []
    for row in result.all():
      result_dicts.append(dict(row._mapping))
    return result_dicts


  

  
  

