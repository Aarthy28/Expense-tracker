from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_expense():
    expense = request.form['expense']
    amount = request.form['amount']
    # Here, you can store data or print it temporarily
    print(f"Expense: {expense}, Amount: {amount}")
    return "Expense added successfully!"

if __name__ == '__main__':
    app.run(debug=True)
