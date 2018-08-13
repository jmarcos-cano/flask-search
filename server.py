from nocache import *
from flask import Flask, render_template, request
app = Flask(__name__)

fak_redis_result=[
    1,
    2,
    3,
    4
]


@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('index.html', search_placeholder="Enter your search ..")

@app.route('/search', methods=['GET', 'POST'])
@nocache
def search():
    #return "Hello {}".format(request.form['search_input'])
    return render_template('results.html', search_input=request.form['search_input'])

@app.route('/results')
@nocache
def results():
    return render_template('results.html')

if __name__ == "__main__":
    app.run()
