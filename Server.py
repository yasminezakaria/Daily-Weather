from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from backend import WeatherAPI

app = Flask(__name__)
Bootstrap(app)

main = WeatherAPI.format_add

@app.route('/')
def index():
    return render_template('index.html', main=main)


if __name__ == '__main__':
    app.run(debug=True)