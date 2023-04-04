from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://8fwmgk3ybnzhbmfmluoz:pscale_pw_XlDJqpWhk9tQaaIaTHnNwGVlNX3gLVnQRvTWHIMGiYu@aws.connect.psdb.cloud/carem-website?charset=utf8mb4"

engine = create_engine(db_connection_string,
                      connect_args={
                        "ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem" 
                        }
                      })

with engine.connect() as conn:
  result = conn.execute(text("select * from plans"))

result_dicts = []
for row in result.all():
  result_dicts.append(row._asdict())
print(result_dicts)


#  print("type(result):",type(result))
#  result_all=result.all()
#  print("type(result.all())", type(result_all))
#  print("result.all():",result_all)
#  first_result = result_all[0]
#  print("type(first_result:)",type(first_result))
#  first_result_dict = result_all[0]._asdict()
#  print("type(first_result_dict:)",type(first_result_dict))
#  print(first_result_dict)