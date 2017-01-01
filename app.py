import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)

def get_csv():
    csv_path =  './static/la-riots-deaths.csv'
    csv_file = open(csv_path, 'rb')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)

@app.route ('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    return render_template(template)

if __name__ == '__main__':
    #Fire up the Flask test erver
    app.run(debug=True, use_reloader=True)
