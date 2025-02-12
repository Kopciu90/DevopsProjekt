from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'

@app.route('/devops')
def devopsTest():
    return '<h1>Devops Test</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)