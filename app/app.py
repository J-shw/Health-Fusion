from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@db:5432/health_fusion'
db = SQLAlchemy(app)

import models # Import models.py

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data')
def process_data():
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    with open(os.path.join(data_dir, 'processed_data.txt'), 'w') as f:
        f.write('Data processed and stored successfully!')

    return "Data processed and stored!"


if __name__ == '__main__':
    app.run(debug=False, port=8080, host='0.0.0.0')