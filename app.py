from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pyzbar.pyzbar import decode
from PIL import Image
import io

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan-barcode', methods=['POST'])
def scan_barcode():
    file = request.files['image']
    image = Image.open(io.BytesIO(file.read()))
    decoded_objects = decode(image)
    barcodes = [obj.data.decode('utf-8') for obj in decoded_objects]
    return jsonify(barcodes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=('cert.pem', 'key.pem'))