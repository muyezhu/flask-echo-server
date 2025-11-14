from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')

    if not expression:
        return jsonify({'result': ''})

    # Basic security check: only allow numbers and operators
    allowed_chars = "0123456789.+-*/() "
    if not all(c in allowed_chars for c in expression):
        return jsonify({'error': 'Invalid characters'}), 400

    try:
        # Evaluate the expression
        # Using eval() with restricted globals/locals is a common way for simple calculators
        # but still has risks if not carefully sanitized.
        # Ideally we would use a proper expression parser.
        # Given the strict character whitelist, it's relatively safe from code execution.
        result = eval(expression, {"__builtins__": None}, {})
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': 'Error calculating'}), 400

if __name__ == '__main__':
    app.run(debug=False, port=5001)
