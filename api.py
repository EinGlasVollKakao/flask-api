import flask
from flask import request, abort

app = flask.Flask(__name__)
app.config.from_pyfile('config.py')


# check app key
@app.before_request
def check_app_key():
    key = request.headers.get('key')
    if key != app.config['API_KEY']:
        abort(401)


@app.route('/', methods=['Get'])
def home():
    return "Jo heee"


# app.run(ssl_context='adhoc')

sys = {
    "temp": "djfsoijfoidf",
    "lel": {
        "manuel": "doof"
    }
}
print(sys["lel"]["manuel"])
