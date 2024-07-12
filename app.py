from flask import Flask, request, redirect, url_for, send_file, render_template, jsonify
import pandas as pd
import os
import time  # Import time module for artificial delay
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['CONVERTED_FOLDER'] = 'converted/'

# Ensure upload and converted folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['CONVERTED_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    delimiter = request.form['delimiter']
    file = request.files['file']
    if file and file.filename.endswith('.csv'):
        filename = secure_filename(file.filename)
        csv_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        xlsx_path = os.path.join(app.config['CONVERTED_FOLDER'], filename.rsplit('.', 1)[0] + '.xlsx')
        
        # Save the uploaded CSV file
        file.save(csv_path)
        
        # Simulate a delay for demonstration purposes (replace with actual conversion logic)
        time.sleep(5)  # Simulate a 5-second conversion
        
        # Read CSV and convert to XLSX
        df = pd.read_csv(csv_path, sep=delimiter, low_memory=False)
        df.to_excel(xlsx_path, index=False)
        
        # Provide the URL for the converted file
        return jsonify({'download_url': url_for('download_file', filename=os.path.basename(xlsx_path))})

    return jsonify({'error': 'Invalid file type'})

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['CONVERTED_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7001))
    app.run(debug=True, host='0.0.0.0', port=port)
