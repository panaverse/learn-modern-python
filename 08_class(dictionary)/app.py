from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    d = {'left': 0.17037454, 'right': 0.82339555, '_unknown_': 0.0059609693}
    message = {
        'status': 200,
        'message': 'OK',
        'scores': d
    }
    resp = jsonify(message)
    print(type(resp))
    resp.status_code = 200
    print(resp)
    return resp

if __name__ == '__main__':
    app.run()