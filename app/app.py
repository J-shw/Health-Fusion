from flask import Flask, render_template
import os


app = Flask(__name__)

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
    app.run(debug=True)