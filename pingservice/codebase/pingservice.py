from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/v1/ping', methods = ["POST"])
def ping():
    response = {"code" : "", "message" : "", "data" : []}
    try:
        data = request.get_json()
        request_url = str(data['url'])
        request_response = requests.get(request_url)
        response['code'] = 200
        response['data'] = request_response.json()
        response['message'] = "Success"
        return jsonify(response)
    except Exception as e:
        response['code'] = 500
        response['data'] = []
        response['message'] = str(e)
        return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
