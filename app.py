from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pathloss')
def pathloss():
    return render_template('pathloss.html')

@app.route('/generate_diagram', methods=['POST'])
def generate_diagram():
    data = request.json
    system_type = data.get('system_type')
    num_rx = data.get('num_rx')
    num_tx = data.get('num_tx')

    # Validate inputs
    if system_type == 'SIMO' and num_rx is not None:
        return jsonify({
            'system_type': 'SIMO',
            'num_rx': int(num_rx),
            'num_tx': 1
        })
    elif system_type == 'MISO' and num_tx is not None:
        return jsonify({
            'system_type': 'MISO',
            'num_tx': int(num_tx),
            'num_rx': 1
        })
    else:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/calculate_path_loss', methods=['GET'])
def calculate_path_loss():
    try:
        distance = float(request.args.get('distance', 1))
        frequency = float(request.args.get('frequency', 900))  # Default to 900 MHz
        if distance <= 0 or frequency <= 0:
            return jsonify({'error': 'Distance and frequency must be positive'}), 400

        # Free Space Path Loss formula
        path_loss = 20 * math.log10(distance) + 20 * math.log10(frequency) - 147.55
        return jsonify({'path_loss': round(path_loss, 2)})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
