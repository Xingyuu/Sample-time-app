from flask import Flask
app = Flask(__name__)
import datetime


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def time():
    now = datetime.datetime.now()
    return(now.strftime("%Y-%m-%d %H:%M:%S"))

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
