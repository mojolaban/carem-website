from flask import Flask, render_template, jsonify, request, json
from database import load_plans_from_db, SAMPLE_PLAN, add_plan_to_db
#from dateutil.parser import parse
#from dateutil import parser
from datetime import datetime

#from sqlalchemy import text

app = Flask(__name__) 

@app.route("/")
def hello_carem():
#  planslist = load_plans_from_db
  return render_template('home.html', plans=SAMPLE_PLAN)

@app.route("/api/sample_plan")
def sample_plan():
  return jsonify(SAMPLE_PLAN)

@app.route("/show")
def show_plan():
  return render_template('show_plan.html')

@app.route("/make")
def make_plan():
  return render_template('make_plan.html')


@app.route("/show", methods=['post']) #show plans already jotted down
def show_made_plan():
  data = request.form
  mark = jsonify(data['mark']).get_data(as_text=
                                        True).strip().strip('"')
  thedate = datetime.strptime(jsonify(data['thedate']).
                              get_data(as_text=True).strip().strip('"'), 
                              '%Y-%m-%d').date()
  return render_template('show_plan.html',data=
                         load_plans_from_db(mark,thedate))

@app.route('/make/committed', methods=['post'])
def committed_plan():
  data = request.form
  add_plan_to_db(data)
  return render_template('plan_committed.html')


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)