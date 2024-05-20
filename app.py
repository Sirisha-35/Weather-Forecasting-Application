from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

# Define the path to the data directory
data_dir = os.path.join(os.path.dirname(__file__), 'data')

# Serve files from the data directory
@app.route('/data/<date>/<city>')
def serve_data(date, city):
    filename = f'rain_temp_{date}_{city}.csv'
    return send_from_directory(data_dir, filename)

# Render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
