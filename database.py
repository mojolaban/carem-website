from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['db_connection_string']

engine = create_engine(db_connection_string,
                      connect_args={
                        "ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem" 
                        }
                      })


def load_plans_from_db():
  with engine.connect() as conn:
    result = conn.execute (text("select * from plans"))
    planslist = []
    for row in result.all():
      planslist.append(row._asdict())
    return planslist


#with engine.connect() as conn:
#  result = conn.execute(text("select * from plans"))

#result_dicts = []
#for row in result.all():
#  result_dicts.append(row._asdict())
#print(result_dicts)


#  print("type(result):",type(result))
#  result_all=result.all()
#  print("type(result.all())", type(result_all))
#  print("result.all():",result_all)
#  first_result = result_all[0]
#  print("type(first_result:)",type(first_result))
#  first_result_dict = result_all[0]._asdict()
#  print("type(first_result_dict:)",type(first_result_dict))
#  print(first_result_dict)

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
