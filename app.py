from flask import Flask,render_template,request,jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/add-expense',methods=['POST'])
def add_expense():
    try:
        data = request.get_json()
        category = data.get('category')
        amount = data.get('amount')
        description = data.get('description')
        return jsonify({'message':'Expense added successfully!'}),200
    except Exception as e: return jsonify({'error':str(e)}),400
if __name__ == '__main__':
    app.run(debug=True)
    