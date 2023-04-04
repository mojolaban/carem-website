from flask import Flask, render_template, jsonify
from database import load_plans_from_db, SAMPLE_PLAN
#from sqlalchemy import text

app = Flask(__name__) 

@app.route("/")
def hello_carem():
#  planslist = load_plans_from_db
  return render_template('home.html', plans=SAMPLE_PLAN)

@app.route("/do")
def planning():
  return jsonify(PLANS)

@app.route("/show")
def show_plan():
  return render_template('show_plan.html')


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)