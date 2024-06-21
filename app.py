from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
sessions = [] 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    start_time = datetime.now()
    sessions.append({'start': start_time, 'end': None, 'break': []})
    return redirect(url_for('index'))

@app.route('/end', methods=['POST'])
def end():
    end_time = datetime.now()
    if sessions and sessions[-1]['end'] is None:
        sessions[-1]['end'] = end_time
    return redirect(url_for('index'))

@app.route('/break_start', methods=['POST'])
def break_start():
    if sessions and sessions[-1]['end'] is None:
        sessions[-1]['break'].append({'start': datetime.now(), 'end': None})
    return redirect(url_for('index'))

@app.route('/break_end', methods=['POST'])
def break_end():
    if sessions and sessions[-1]['end'] is None and sessions[-1]['break'] and sessions[-1]['break'][-1]['end'] is None:
        sessions[-1]['break'][-1]['end'] = datetime.now()
    return redirect(url_for('index'))

@app.route('/report')
def report():
    return render_template('report.html', sessions=sessions)

if __name__ == '__main__':
    app.run(debug=True)