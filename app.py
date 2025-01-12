from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory expenses list (temporary storage)
expenses = []

# Home route to display the expense form and the list of expenses
@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)

# Route to handle the form submission and add the expense
@app.route('/add', methods=['POST'])
def add_expense():
    # Get data from the form
    category = request.form['category']
    amount = request.form['amount']
    description = request.form['description']

    # Create a dictionary to represent the expense
    expense = {
        'category': category,
        'amount': amount,
        'description': description
    }

    # Add the expense to the list
    expenses.append(expense)

    # Redirect back to the homepage to see the updated list
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
