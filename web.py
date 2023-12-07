import csv
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/homePage')
def index():
    return render_template('homePage.html')

@app.route('/')
def hello_world(): 
    return 'nihao!'

@app.route('/api/mydata', methods=['GET'])
def api_mydata():
    data = get_data()
    return jsonify(data)


@app.route('/us-cities/<name>')
def city(name):
    with open('static/us-cities.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['city'] == name:
                return render_template('us-cities.html', **row)
        return "City not found", 404

def get_data():
    data = []
    with open('static/amazon-reviews.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data




if __name__ == '__main__':
    app.run()
