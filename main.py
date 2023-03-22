import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = 'a'
    name = request.form.get('name')
    class_ = request.form.get('class')
    email = request.form.get('email')
    place = request.form.get('place')
    area = request.form.get('area')
    rating = request.form.get('rating')
    feedback = request.form.get('feedback')
  
    if(feedback == 'Easter egg' or 'easter egg' or 'Easter Egg'):
		    data = 'egg'
    elif(feedback == 'disappointed' or 'upset' or 'angry'):
        data = 'feelings'
    elif(feedback == 'nil' or 'nope' or 'no' or 'nah'):
        data = 'next'
      
    with open('submission.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([name, email, class_, rating, feedback])
    return redirect(url_for('success', name=name, data=data))
    csvfile.close()
  
@app.route('/success/<name>, <data>')
def success(name, data):
    return render_template('html.html', name=name, data=data)


app.run(host='0.0.0.0', port=81)
