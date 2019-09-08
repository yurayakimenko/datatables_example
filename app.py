from flask import Flask, jsonify, render_template, request
from random import randrange
import utils
from datetime import datetime, timedelta

app = Flask(__name__)

db_rows = [
    # {"id": 1, "area": 200.23, "price": 32000000, "currency": "UAH", "description": "Крутой особняк"},
    # {"id": 2, "area": 89, "price": 32000, "currency": "UAH", "description": "Дача"}
]

for i in range(300):
    db_rows.append({"id": i, "area": randrange(20, 200), "price": randrange(1000000, 99999999999), "currency": "UAH", "description": ""})

@app.route('/mydata')
def mydata():
    # Поменяли на .args, потому что у нас теперь GET запросы
    period = request.args.get('period')
    start, end = utils.parse_start_end(period)
    # Используй полученные start и end при фильтрации из базы.
    # Т.к. для примера нет базы, то оставляю это так.
    if period == 'day':
        display_rows = db_rows[:30]
    elif period == 'week':
        display_rows = db_rows[30:100]
    else:
        display_rows = db_rows
    return jsonify({"data": display_rows})


@app.route('/')
def index():
    return render_template('index.html',
                           today=datetime.now().strftime('%d/%m/%Y'),
                           start=(datetime.now()-timedelta(days=5)).strftime('%d/%m/%Y'))


app.run(host='localhost', port=8080, debug=True)
