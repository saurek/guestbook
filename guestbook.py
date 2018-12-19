from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sign')
def sign():
    return render_template('sign.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    links = ['https://google.com', 'https://www.shodan.io/', 'https://meduza.io/en', 'https://informnapalm.org/en/']
    return render_template('example.html', zevar='', links=links)


if __name__ == '__main__':
    app.run(debug=True)
