from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)
 
 #Database Model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default= lambda: datetime.now(timezone.utc))


@app.route('/',methods=['GET', 'POST'])  
def index():
    if request.method == "POST":
        title = request.form.get('title', '').strip()
        amount_raw = request.form.get('amount', '0')
        category = request.form.get('category', 'General')

        if title and amount_raw:
            try:
                new_expense = Expense(
                    title = title,
                    amount = float(amount_raw),
                    category = category
                )
                db.session.add(new_expense)
                db.session.commit()
            except ValueError:
                pass
        return redirect(url_for('index'))

    #Fetch expense and calculate summary figures
    expenses = Expense.query.order_by(Expense.created_at.desc()).all()
    total_spent = sum(item.amount for item in expenses)

    #Category aggretion for calculator breakdown
    category_totals = {}
    for item in expenses:
        category_totals[item.category] = category_totals.get(item.category, 0.0) + item.amount

    return render_template(
        'index.html',
        expenses  = expenses,
        total_spent = total_spent,
        category_totals = category_totals
    )


@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    expense = db.session.get(Expense, expense_id)
    if expense:
        db.session.delete(expense)
        db.session.commit()
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    


    
