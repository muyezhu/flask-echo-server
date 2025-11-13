from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if not isinstance(data, dict) or 'numbers' not in data or not isinstance(data['numbers'], list):
        return jsonify({"error": "Invalid input. 'numbers' key with a list of numbers is required."}), 400

    numbers = data['numbers']
    if not all(isinstance(n, (int, float)) for n in numbers):
        return jsonify({"error": "All items in 'numbers' must be numeric."}), 400

    return jsonify({"sum": sum(numbers)})

if __name__ == "__main__":
    app.run(debug=True)

