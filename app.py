from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True)