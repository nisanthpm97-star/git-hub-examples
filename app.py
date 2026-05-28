from flask import Flask, jsonify, render_template
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

@app.route('/api', methods=['GET'])
def get_data():
    if not os.path.exists(DATA_FILE):
        return jsonify({"error": "Data file not found"}), 404
    
    try:
        
        with open(DATA_FILE, 'r') as file:
            data = json.load(file) 
        
        return jsonify(data)
    
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON in data file"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)