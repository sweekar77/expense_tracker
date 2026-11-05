@pytest.fixture
def client():
    # Configure app for isolated testing in memory
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as test_client:
        with app.app_context():
            db.create_all()
            yield test_client
            db.session.remove()
            db.drop_all()

# --- GET / (Index page) Tests ---

def test_index_empty_state(client):
    """Verify that an empty database displays the correct placeholder text."""
    response = client.get('/')
    assert response.status_code == 200
    html = response.data.decode('utf-8')
    assert "Expense Tracker" in html
    assert "No expenses logged yet." in html
    assert "$0.00" in html

def test_index_with_existing_data(client):
    """Verify expenses are displayed correctly in the ledger table."""
    with app.app_context():
        item = Expense(title="Lunch", amount=12.50, category="Food & Dining")
        db.session.add(item)
        db.session.commit()

    response = client.get('/')
    assert response.status_code == 200
    html = response.data.decode('utf-8')
    assert "Lunch" in html
    assert "$12.50" in html
    assert "Food & Dining" in html

# --- POST / (Create Expense) Tests ---

def test_create_expense_valid(client):
    """Verify posting valid form data inserts a record and redirects."""
    payload = {
        'title': 'Bus Pass',
        'amount': '45.00',
        'category': 'Transportation'
    }
    response = client.post('/', data=payload, follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        expense = Expense.query.filter_by(title='Bus Pass').first()
        assert expense is not None
        assert expense.amount == 45.00
        assert expense.category == 'Transportation'

    html = response.data.decode('utf-8')
    assert "Bus Pass" in html
    assert "$45.00" in html

def test_create_expense_invalid_amount(client):
    """Verify non-numeric values do not create a database record."""
    payload = {
        'title': 'Broken Data',
        'amount': 'invalid_number',
        'category': 'General'
    }
    response = client.post('/', data=payload, follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        count = Expense.query.count()
        assert count == 0

def test_create_expense_empty_title(client):
    """Verify whitespace-only titles are rejected."""
    payload = {
        'title': '   ',
        'amount': '25.00',
        'category': 'Utilities'
    }
    response = client.post('/', data=payload, follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        count = Expense.query.count()
        assert count == 0

# --- Expense Calculator & Aggregation Tests ---

def test_expense_totals_and_breakdowns(client):
    """Verify total sum and category aggregation logic."""
    with app.app_context():
        e1 = Expense(title="Dinner", amount=30.00, category="Food & Dining")
        e2 = Expense(title="Coffee", amount=5.50, category="Food & Dining")
        e3 = Expense(title="Internet", amount=60.00, category="Utilities")
        db.session.add_all([e1, e2, e3])
        db.session.commit()

    response = client.get('/')
    html = response.data.decode('utf-8')

    # Total should be 30 + 5.5 + 60 = 95.50
    assert "$95.50" in html
    # Food & Dining: 35.50
    assert "$35.50" in html
    # Utilities: 60.00
    assert "$60.00" in html

# --- POST /delete/<id> Tests ---

def test_delete_expense_success(client):
    """Verify an existing expense can be removed."""
    with app.app_context():
        item = Expense(title="Snack", amount=3.00, category="Food & Dining")
        db.session.add(item)
        db.session.commit()
        item_id = item.id

    response = client.post(f'/delete/{item_id}', follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        deleted = db.session.get(Expense, item_id)
        assert deleted is None

def test_delete_non_existent_expense(client):
    """Verify attempting to delete a non-existent ID fails gracefully."""
    response = client.post('/delete/9999', follow_redirects=True)
    assert response.status_code == 200