from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:///expense.dv'
app.config['SQALCHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)
 
 #Database Model
class Expense(db.model):
    id = db.column(db.integer, primary_keys=True)
    title = db.column(db.string(100), nullable=False)
    amount = db.column(db.Float, nullable=False)
    ctegory = db.column(db.string(50), nullable=False)
    created_at = db.column(db.datatime, default= lambda: datetime.now(timezone.utc))


@app.route('/',methods=['GET', 'POST'])  
def index():
    if request.method == "POST":
        title = request.form.get('title', '').strip()
        amount_raw = request.form.get('category', 'General')

        if title and amount_raw:
            try:
                new_expense = Expense(
                    title = title,
                    amount = float(amount_raw)
                )
                db.session.add(new.expense)
                db.session.commit
            except ValueError:
                pass
            return redirect(url_for(index))

        #Fetch expense and calculate summary figures
        expenses = Expense.query.order_by(Expense.created_at.desc()).all()
        total_spent = sum(item.amount for item in expenses)

        #Category aggretion for calculator breakdown
        category_total = {}
        for item in expenses:
            category_totals[item.category] = category_totals.get(item.category, 0.0) + item.ammount

        return render_template(
            'index.html',
            expenses  = expenses,
            total_spent = total_spent,
            category_total = category_total
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
    


    
