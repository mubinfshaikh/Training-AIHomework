from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/v1/info', methods = ["GET"])
def ping():
    response = {"Receiver": "Cisco is the best!"}
    try:
        return jsonify(response)
    except Exception as e:
        return jsonify(response)

if __name__ == '__main__':
    app.run(port=5001)
