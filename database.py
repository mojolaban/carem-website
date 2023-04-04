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

SAMPLE_PLAN = [
  {
    'id' : 1,
    'date' : '01-04-2023',
    'yesterday' : 'Started data extraction on 1 article',
    'today' : 'Research sources of systematic literature review and choose one method',
    'tomorrow': 'Conduct more (at least 10) article data extractions',
    'mark' : 'auniquecode'
  },
    {
    'id' : 2,
    'date' : '02-04-2023',
    'yesterday' : 'Chose content analysis as the framework for data synthesis',
    'today' : 'Conduct 10 data extractions on selected articles',
    'tomorrow': 'Start to remove articles with low quality rigor and unclear findings',
    'mark' : 'moreuniquecode'
  },
    {
    'id' : 3,
    'date' : '03-04-2023',
    'yesterday' : 'Done extracting 17 data extractions',
    'today' : 'Constructing parameters of quality articles, and selecting articles to be removed',
    'tomorrow': 'Continue data extractions (minimum 20)',
    'mark' : 'anotheruniquecode'
  }
]