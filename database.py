from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['db_connection_string']

engine = create_engine(db_connection_string,
                      connect_args={
                        "ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem" 
                        }
                      })

def load_plans_from_db(mark,thedate):
  with engine.connect() as conn:
    result = conn.execute (text("select * from plans where mark= :mark and thedate= :thedate"),{"mark":mark,"thedate":thedate})
    rows=result.all()
    if len(rows)==0:
      return None
    else:
      return rows[0]._asdict()

def add_plan_to_db(data):
  with engine.connect() as conn:
    query = text("INSERT into plans (thedate, today, yesterday, tomorrow, mark) values (:thedate, :today, :yesterday, :tomorrow, :mark)")
    conn.execute(query,
    [
    {"thedate":data['thedate'],
    "today":data['today'],
    "yesterday":data['yesterday'],
    "tomorrow":data['tomorrow'],
    "mark":data['mark']}
    ]
    )