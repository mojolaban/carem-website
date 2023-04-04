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