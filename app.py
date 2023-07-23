from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title' : 'Software Engineer',
    'location' : 'Kolkata, India',
    'salary' : 'Rs 100000'
  },
  {
    'id' : 2,
    'title' : 'Data Scientist',
    'location' : 'Bengaluru, India',
    'salary' : 'Rs 200000'
  },
  {
    'id' : 3,
    'title' : 'Data Analyst',
    'location' : 'Remote'
  },
  {
    'id' : 4,
    'title' : 'Graphic Designer',
    'location' : 'Chennai, India',
    'salary' : 'Rs 300000'
  }
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__" :
  app.run(host='0.0.0.0',debug=True)