from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

@app.route('/echo_xyz', methods=['GET'])
def echo_xyz():
    return jsonify({"xyz": "xyz"})

if __name__ == "__main__":
    app.run(debug=True)

