from flask import Flask, jsonify, render_template, request
from random import randrange

app = Flask(__name__)

db_rows = [
    # {"id": 1, "area": 200.23, "price": 32000000, "currency": "UAH", "description": "Крутой особняк"},
    # {"id": 2, "area": 89, "price": 32000, "currency": "UAH", "description": "Дача"}
]

for i in range(300):
    db_rows.append({"id": i, "area": randrange(20, 200), "price": randrange(1000000, 99999999999), "currency": "UAH", "description": ""})


@app.route('/mydata', methods=['POST'])
def mydata():
    mode = request.form.get('mode')
    if mode == 'day':
        display_rows = db_rows[:30]
    elif mode == 'week':
        display_rows = db_rows[30:100]
    else:
        display_rows = db_rows
    return jsonify(display_rows)


@app.route('/')
def index():
    return render_template('index.html')


app.run(host='localhost', port=8080, debug=True)
