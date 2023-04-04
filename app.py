from flask import Flask, render_template, jsonify
from database import load_plans_from_db
#from sqlalchemy import text

app = Flask(__name__) 

PLANS = [
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


@app.route("/")
def hello_carem():
#  planslist = load_plans_from_db
  return render_template('home.html', plans=PLANS)

@app.route("/do")
def planning():
  return jsonify(PLANS)

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)