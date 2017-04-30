#!flask/bin/python
from flask import abort, Flask, jsonify, request

app = Flask(__name__)

counter = 0

@app.route('/api/v1/counter', methods=['GET'])
def getCounter():
    # if 'id' in request.args: request.args['id'].first()
    return jsonify({'counter': counter})

@app.route('/api/v1/counter', methods=['POST'])
def create_item():
    global counter
    counter = counter + 1
    return jsonify({'counter': counter})

if __name__ == '__main__':
    app.run(debug=True)