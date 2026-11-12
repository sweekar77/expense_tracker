
import os

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ==========================================
# FLASK CONFIGURATION
# ==========================================

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# ==========================================
# DATABASE MODEL
# ==========================================

class Expense(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc)
    )


# ==========================================
# CHART DIRECTORY
# ==========================================

static_dir = os.path.join(app.root_path, 'static')
os.makedirs(static_dir, exist_ok=True)


# ==========================================
# PIE CHART GENERATION
# ==========================================

def create_pie_chart():

    chart_path = os.path.join(
        static_dir, 'expenses_chart.png'
    )

    results = db.session.query(
        Expense.category,
        db.func.sum(Expense.amount)
    ).group_by(Expense.category).all()

    if not results or sum(float(row[1]) for row in results) <= 0:

        if os.path.exists(chart_path):
            os.remove(chart_path)

        return False

    categories = [row[0] for row in results]
    amounts = [float(row[1]) for row in results]

    plt.figure(figsize=(6, 6))

    plt.pie(
        amounts,
        labels=categories,
        autopct="%1.1f%%"
    )

    plt.title("Expenses by Category")

    plt.savefig(chart_path, bbox_inches='tight')
    plt.close()

    return True


# ==========================================
# BAR CHART GENERATION
# ==========================================

def create_bar_chart():

    chart_path = os.path.join(
        static_dir, 'barchart.png'
    )

    results = db.session.query(
        Expense.category,
        db.func.sum(Expense.amount)
    ).group_by(Expense.category).all()

    if not results or sum(float(row[1]) for row in results) <= 0:

        if os.path.exists(chart_path):
            os.remove(chart_path)

        return False

    categories = [row[0] for row in results]
    amounts = [float(row[1]) for row in results]

    plt.figure(figsize=(8, 5))

    plt.bar(categories, amounts)

    plt.xlabel("Expense Categories")
    plt.ylabel("Amount Spent")
    plt.title("Expenses by Category")

    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()

    plt.savefig(chart_path, bbox_inches='tight')
    plt.close()

    return True


# ==========================================
# HOME PAGE
# ==========================================

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":

        title = request.form.get('title', '').strip()
        amount_raw = request.form.get('amount', '0')
        category = request.form.get('category', 'General').strip()

        if title and amount_raw and category:

            try:
                amount = float(amount_raw)

                if amount > 0:

                    new_expense = Expense(
                        title=title,
                        amount=amount,
                        category=category
                    )

                    db.session.add(new_expense)
                    db.session.commit()

            except ValueError:
                db.session.rollback()

        return redirect(url_for('index'))

    # Fetch expenses
    expenses = Expense.query.order_by(
        Expense.created_at.desc()
    ).all()

    # Calculate total expenditure
    total_spent = sum(
        item.amount for item in expenses
    )

    # Calculate category totals
    category_totals = {}

    for item in expenses:

        category_totals[item.category] = (
            category_totals.get(item.category, 0.0)
            + item.amount
        )

    # Generate charts
    chart_created = create_pie_chart()
    bar_chart_created = create_bar_chart()

    return render_template(
        'index.html',
        expenses=expenses,
        total_spent=total_spent,
        category_totals=category_totals,
        chart_created=chart_created,
        bar_chart_created=bar_chart_created
    )


# ==========================================
# DELETE EXPENSE
# ==========================================

@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):

    expense = db.session.get(Expense, expense_id)

    if expense:

        db.session.delete(expense)
        db.session.commit()

    return redirect(url_for('index'))


# ==========================================
# DATABASE INITIALIZATION
# ==========================================

with app.app_context():
    db.create_all()


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == '__main__':
    app.run(debug=True)


    
