from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

expenses = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    data = request.json
    expenses.append(data)
    return jsonify(expenses), 201

@app.route('/get_expenses', methods=['GET'])
def get_expenses():
    return jsonify(expenses)

if __name__ == '__main__':
    app.run(debug=True)
