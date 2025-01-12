from flask import Flask, render_template, request

app = Flask(__name__)

# Global variable to store expenses
expenses = []

@app.route('/')
def home():
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    category = request.form['category']
    amount = request.form['amount']
    description = request.form['description']
    
    # Add expense to the list
    expenses.append({
        'category': category,
        'amount': float(amount),
        'description': description
    })
    return render_template('index.html', expenses=expenses)

if __name__ == '_main_':
    app.run(debug=True)