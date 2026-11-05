Welcome to my first program

To get started activate my virtual environment
.\.venv\Scripts\Activate.ps1 

To run the program
python app.py

style.css

/* --------------------------------------------------
   1. ROOT VARIABLES
-------------------------------------------------- */

/*
   :root represents the highest-level element in the HTML document.

   We define CSS variables here so that we can reuse
   colors and styles throughout the stylesheet.

   var(--variable-name) is used to access these variables.
*/

:root {

    /* Background colors */
    --bg-main: #f0fdf4;       /* Main webpage background */
    --card-bg: #ffffff;       /* Background of cards */
    --input-bg: #f8fafc;      /* Background of input fields */

    /* Border colors */
    --border: #dcfce7;        /* Color of borders */

    /* Green theme colors */
    --accent: #16a34a;        /* Main green color */
    --accent-hover: #15803d;  /* Green color when hovering */
    --dark-green: #166534;    /* Dark green for headings */
    --light-green: #bbf7d0;   /* Light green for badges */

    /* Status colors */
    --danger: #ef4444;        /* Color for delete actions */
    --danger-hover: #dc2626;  /* Darker red when hovering */

    /* Text colors */
    --text-primary: #14532d;  /* Main text color */
    --text-secondary: #64748b;/* Secondary text color */

    /* Shadow */
    --shadow: 0 4px 12px rgba(22, 101, 52, 0.08);
    /* Adds a subtle shadow around cards */
}


/* --------------------------------------------------
   2. UNIVERSAL SELECTOR
-------------------------------------------------- */

/*
   The * selector targets every HTML element.

   box-sizing: border-box:
   Includes padding and borders within an element's total width.

   margin: 0:
   Removes default outside spacing.

   padding: 0:
   Removes default inside spacing.

   font-family:
   Defines the fonts used throughout the webpage.
*/

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;

    font-family: -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}


/* --------------------------------------------------
   3. BODY STYLING
-------------------------------------------------- */

/*
   body represents the visible content of the webpage.

   background-color:
   Sets the main background color.

   color:
   Sets the default text color.

   padding:
   Adds space inside the body around its content.
*/

body {
    background-color: var(--bg-main);
    color: var(--text-primary);
    padding: 2rem 1rem;
}


/* --------------------------------------------------
   4. MAIN CONTAINER
-------------------------------------------------- */

/*
   .container selects the HTML element with class="container".

   max-width:
   Prevents the container from becoming wider than 900px.

   margin: 0 auto:
   Centers the container horizontally.

   display: flex:
   Uses Flexbox for arranging child elements.

   flex-direction: column:
   Arranges child elements vertically.

   gap:
   Creates spacing between child elements.
*/

.container {
    max-width: 900px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}


/* --------------------------------------------------
   5. HEADER STYLING
-------------------------------------------------- */

/*
   header h1 selects an h1 element inside the header.

   font-size:
   Controls the heading size.

   font-weight:
   Controls how bold the text appears.

   color:
   Sets the heading color.
*/

header h1 {
    font-size: 1.75rem;
    font-weight: 700;
    color: var(--dark-green);
}


/* --------------------------------------------------
   6. DESCRIPTION SECTION
-------------------------------------------------- */

/*
   .description selects the description container.

   background-image:
   Combines two background layers:

   1. Linear gradient: Adds a transparent green overlay.
   2. URL: Displays the background image.

   background-size: cover:
   Makes the image cover the entire container.

   background-position: center:
   Keeps the image centered.

   padding:
   Adds space inside the description section.

   border-radius:
   Rounds the corners.

   color: white:
   Makes the description text white.
*/

.description {
    background-image:
        linear-gradient(rgba(20, 83, 45, 0.65),
        rgba(20, 83, 45, 0.65)),
        url("/static/premium_photo-1681469490618-c24cc20bef1c.avif");

    background-size: cover;
    background-position: center;
    padding: 30px;
    border-radius: 10px;
    color: white;
}


/* --------------------------------------------------
   7. GENERAL CARD STYLING
-------------------------------------------------- */

/*
   .card applies common styling to card elements.

   background:
   Sets the card background.

   border:
   Adds a border around the card.

   border-radius:
   Rounds the card corners.

   padding:
   Adds internal spacing.

   box-shadow:
   Adds a shadow behind the card.
*/

.card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.25rem;
    box-shadow: var(--shadow);
}


/* --------------------------------------------------
   8. SUMMARY GRID
-------------------------------------------------- */

/*
   .summary-grid arranges the summary cards.

   display: grid:
   Uses CSS Grid.

   grid-template-columns: 1fr 1fr:
   Creates two equal-width columns.

   gap:
   Adds space between the columns.
*/

.summary-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
}


/* --------------------------------------------------
   9. TOTAL EXPENDITURE
-------------------------------------------------- */

/*
   .total-card .stat selects an element with class="stat"
   inside an element with class="total-card".

   font-size:
   Makes the total expenditure number larger.

   font-weight:
   Makes the number bold.

   color:
   Applies the main green accent color.

   margin-top:
   Adds space above the number.
*/

.total-card .stat {
    font-size: 2.25rem;
    font-weight: 700;
    color: var(--accent);
    margin-top: 0.5rem;
}


/* --------------------------------------------------
   10. CATEGORY BREAKDOWN
-------------------------------------------------- */

/*
   .breakdown-list styles the category list.

   margin-top:
   Adds space above the list.

   display: flex:
   Uses Flexbox.

   flex-direction: column:
   Arranges categories vertically.

   gap:
   Adds spacing between category rows.
*/

.breakdown-list {
    margin-top: 0.5rem;
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
}


/*
   .breakdown-row styles each category row.

   display: flex:
   Places category name and amount in one row.

   justify-content: space-between:
   Places the category name on the left
   and its amount on the right.

   font-size:
   Controls text size.

   color:
   Sets secondary text color.
*/

.breakdown-row {
    display: flex;
    justify-content: space-between;
    font-size: 0.95rem;
    color: var(--text-secondary);
}


/* --------------------------------------------------
   11. EXPENSE FORM
-------------------------------------------------- */

/*
   .expense-form controls the arrangement of form fields.

   display: grid:
   Uses CSS Grid.

   grid-template-columns: 2fr 1fr 1.5fr auto:
   Creates four columns with different widths.

   gap:
   Adds spacing between form elements.

   align-items: flex-end:
   Aligns elements along their bottom edges.

   margin-top:
   Adds space above the form.
*/

.expense-form {
    display: grid;
    grid-template-columns: 2fr 1fr 1.5fr auto;
    gap: 1rem;
    align-items: flex-end;
    margin-top: 1rem;
}


/* --------------------------------------------------
   12. FORM GROUPS
-------------------------------------------------- */

/*
   .form-group controls the arrangement of each form field.

   flex-direction: column:
   Places the label above its input.

   gap:
   Adds space between the label and input.
*/

.form-group {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
}


/* --------------------------------------------------
   13. LABEL STYLING
-------------------------------------------------- */

/*
   label selects all HTML label elements.

   font-size:
   Controls label text size.

   color:
   Applies the secondary text color.
*/

label {
    font-size: 0.85rem;
    color: var(--text-secondary);
}


/* --------------------------------------------------
   14. INPUT AND DROPDOWN STYLING
-------------------------------------------------- */

/*
   input selects input fields.
   select selects dropdown menus.

   background:
   Sets their background color.

   border:
   Adds a border.

   color:
   Sets the text color.

   padding:
   Adds internal spacing.

   border-radius:
   Rounds the corners.

   font-size:
   Controls text size.
*/

input, select {
    background: var(--input-bg);
    border: 1px solid var(--border);
    color: var(--text-primary);
    padding: 0.6rem 0.75rem;
    border-radius: 6px;
    font-size: 0.95rem;
}


/* --------------------------------------------------
   15. INPUT FOCUS EFFECT
-------------------------------------------------- */

/*
   :focus is a pseudo-class.

   It applies styling when the user clicks on
   or selects an input or dropdown.

   outline: none:
   Removes the browser's default outline.

   border-color:
   Changes the border to green.
*/

input:focus, select:focus {
    outline: none;
    border-color: var(--accent);
}


/* --------------------------------------------------
   16. GENERAL BUTTON STYLING
-------------------------------------------------- */

/*
   .btn applies common styling to buttons.

   padding:
   Adds space inside the button.

   border: none:
   Removes the default border.

   border-radius:
   Rounds the corners.

   font-weight:
   Makes button text bold.

   cursor: pointer:
   Changes the cursor to a pointer when hovering.

   transition:
   Makes background-color changes smoother.
*/

.btn {
    padding: 0.65rem 1rem;
    border: none;
    border-radius: 6px;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.15s ease;
}


/* --------------------------------------------------
   17. ADD EXPENSE BUTTON
-------------------------------------------------- */

/*
   .primary-btn selects the button used to add expenses.

   background:
   Sets its green background.

   color:
   Makes the button text white.
*/

.primary-btn {
    background: var(--accent);
    color: white;
}


/*
   :hover applies styling when the mouse
   pointer moves over the button.
*/

.primary-btn:hover {
    background: var(--accent-hover);
}


/* --------------------------------------------------
   18. DELETE BUTTON
-------------------------------------------------- */

/*
   .delete-btn styles the delete button.

   background: transparent:
   Makes the background transparent.

   color:
   Sets the text color to red.

   border:
   Adds a red border.

   padding:
   Controls internal spacing.

   font-size:
   Controls text size.
*/

.delete-btn {
    background: transparent;
    color: var(--danger);
    border: 1px solid var(--danger);
    padding: 0.3rem 0.6rem;
    font-size: 0.8rem;
}


/*
   Changes the delete button appearance
   when the user hovers over it.
*/

.delete-btn:hover {
    background: var(--danger);
    color: white;
}


/* --------------------------------------------------
   19. TABLE STYLING
-------------------------------------------------- */

/*
   table selects HTML table elements.

   width: 100%:
   Makes the table use the full available width.

   border-collapse: collapse:
   Combines adjacent table borders.

   margin-top:
   Adds space above the table.

   text-align: left:
   Aligns table content to the left.
*/

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
    text-align: left;
}


/*
   th represents table headings.
   td represents table data cells.

   padding:
   Adds space inside table cells.

   border-bottom:
   Adds a dividing line below each cell.
*/

th, td {
    padding: 0.75rem 0.5rem;
    border-bottom: 1px solid var(--border);
}


/*
   Styles the table headings.
*/

th {
    color: var(--dark-green);
    font-size: 0.85rem;
}


/* --------------------------------------------------
   20. CATEGORY BADGES
-------------------------------------------------- */

/*
   .badge styles the category labels.

   background:
   Applies a light green background.

   color:
   Applies dark green text.

   padding:
   Adds space around the text.

   border-radius:
   Rounds the corners.

   font-size:
   Controls text size.
*/

.badge {
    background: var(--light-green);
    color: var(--dark-green);
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-size: 0.8rem;
}


/* --------------------------------------------------
   21. AMOUNT STYLING
-------------------------------------------------- */

/*
   .amount selects elements displaying expense amounts.

   font-weight:
   Makes the amount bold.

   color:
   Applies dark green.
*/

.amount {
    font-weight: 600;
    color: var(--dark-green);
}


/* --------------------------------------------------
   22. EMPTY STATE
-------------------------------------------------- */

/*
   .empty-state styles messages displayed when
   there are no expenses or categories.

   color:
   Uses secondary text color.

   font-style: italic:
   Makes the text italic.

   font-size:
   Controls text size.
*/

.empty-state {
    color: var(--text-secondary);
    font-style: italic;
    font-size: 0.9rem;
}


/* --------------------------------------------------
   23. RESPONSIVE DESIGN
-------------------------------------------------- */

/*
   @media is a CSS media query.

   max-width: 768px means these styles apply
   when the screen width is 768 pixels or less.

   This helps the application work on smaller
   devices such as tablets and mobile phones.
*/

@media (max-width: 768px) {

    /*
       Changes the summary grid from two columns
       into one column on smaller screens.
    */
    .summary-grid {
        grid-template-columns: 1fr;
    }


    /*
       Changes the expense form into one column.

       Form fields will appear vertically instead
       of horizontally.
    */
    .expense-form {
        grid-template-columns: 1fr;
    }

}

---------------------------------------------------------------------------------------------------------
index.html

<!-- -------------------------------------------------
     1. HTML DOCUMENT STRUCTURE
-------------------------------------------------- -->

<!DOCTYPE html>

<!-- Defines the language of the webpage as English. -->
<html lang="en">

<head>

    <!-- Supports different characters and symbols. -->
    <meta charset="UTF-8">

    <!-- Makes the webpage responsive on different devices. -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Sets the title displayed in the browser tab. -->
    <title>Expense Tracker & Calculator</title>

    <!-- Connects the external CSS file to this HTML page.
         url_for generates the correct path to the static folder. -->
    <link rel="stylesheet"
          href="{{ url_for('static', filename='style.css') }}">

</head>

<body>

    <!-- -------------------------------------------------
         2. MAIN CONTAINER AND HEADER
    -------------------------------------------------- -->

    <!-- Main container groups the introductory content. -->
    <div class="container">

        <!-- Header contains the main heading of the page. -->
        <header>

            <h1>Expense Tracker</h1>

        </header>


        <!-- -------------------------------------------------
             3. APPLICATION DESCRIPTION
        -------------------------------------------------- -->

        <!-- Description section introduces the application. -->
        <div class="description">

            <h3>
                This application helps users record, monitor,
                and manage their daily spending. It helps in:
            </h3>

            <!-- Unordered list displays the application's benefits. -->
            <ul>

                <li><h3>tracking spendings</h3></li>

                <li><h3>budget management</h3></li>

                <li><h3>tracking spendings</h3></li>

                <li><h3>unnecessary expense</h3></li>

                <li><h3>saving money</h3></li>

            </ul>

            <h3>and provides many more advantages</h3>

        </div>

    </div>

    <!-- Creates a horizontal dividing line. -->
    <hr>


    <!-- -------------------------------------------------
         4. SUMMARY CARDS / CALCULATOR METRICS
    -------------------------------------------------- -->

    <!-- Displays summary information about expenses. -->
    <section class="summary-grid">

        <!-- Card displaying total expenditure. -->
        <div class="card total-card">

            <h3>Total Expenditure</h3>

            <!--
                total_spent comes from Python (app.py).

                "%.2f" formats the number to two decimal places.
                The | symbol is called a Jinja2 filter.
            -->
            <p class="stat">
                ${{ "%.2f"|format(total_spent) }}
            </p>

        </div>


        <!-- Card displaying category-wise expenditure. -->
        <div class="card breakdown-card">

            <h3>Category Breakdown</h3>

            <div class="breakdown-list">

                <!--
                    Loops through the category_totals dictionary.

                    cat = Category name (key).
                    amt = Total amount spent (value).
                -->
                {% for cat, amt in category_totals.items() %}

                    <div class="breakdown-row">

                        <!-- Displays the category name. -->
                        <span>{{ cat }}</span>

                        <!-- Displays the total amount for that category. -->
                        <strong>
                            ${{ "%.2f"|format(amt) }}
                        </strong>

                    </div>

                <!-- Executes if the dictionary is empty. -->
                {% else %}

                    <p class="empty-state">
                        No categories recorded yet.
                    </p>

                <!-- Ends the for loop. -->
                {% endfor %}

            </div>

        </div>

    </section>


    <!-- -------------------------------------------------
         5. EXPENSE ENTRY FORM
    -------------------------------------------------- -->

    <!-- Section containing the form for adding expenses. -->
    <section class="card form-card">

        <h2>Add New Expense</h2>

        <!--
            method="POST" sends the form information to Flask.

            action="/" sends the information to the homepage route.
        -->
        <form method="POST" action="/" class="expense-form">


            <!-- Expense description input. -->
            <div class="form-group">

                <label for="title">Description</label>

                <!--
                    type="text": Accepts text.
                    id: Identifies this input in HTML.
                    name: Identifies the input when Flask receives it.
                    required: Prevents submission when empty.
                -->
                <input
                    type="text"
                    id="title"
                    name="title"
                    placeholder="e.g. Groceries"
                    required
                >

            </div>


            <!-- Expense amount input. -->
            <div class="form-group">

                <label for="amount">Amount ($)</label>

                <!--
                    type="number": Accepts numerical values.
                    step="0.01": Allows two decimal places.
                    name="amount": Flask uses this name to retrieve the value.
                -->
                <input
                    type="number"
                    step="0.01"
                    id="amount"
                    name="amount"
                    placeholder="0.00"
                    required
                >

            </div>


            <!-- Expense category selection. -->
            <div class="form-group">

                <label for="category">Category</label>

                <!-- Dropdown menu allows users to select a category. -->
                <select id="category" name="category">

                    <option value="Food & Dining">
                        Food & Dining
                    </option>

                    <option value="Transportation">
                        Transportation
                    </option>

                    <option value="Utilities">
                        Utilities
                    </option>

                    <option value="Entertainment">
                        Entertainment
                    </option>

                    <option value="General">
                        General
                    </option>

                </select>

            </div>


            <!-- Submits the expense information to Flask. -->
            <button type="submit" class="btn primary-btn">
                Add Expense
            </button>

        </form>

    </section>


    <!-- -------------------------------------------------
         6. RECENT EXPENSES TABLE
    -------------------------------------------------- -->

    <!-- Displays previously recorded expenses. -->
    <section class="card table-card">

        <h2>Recent Expenses</h2>

        <table>

            <!-- Table heading section. -->
            <thead>

                <tr>
                    <th>Item</th>
                    <th>Category</th>
                    <th>Date</th>
                    <th>Amount</th>
                    <th>Action</th>
                </tr>

            </thead>


            <!-- Table body containing expense records. -->
            <tbody>

                <!--
                    Loops through the expenses list received from Python.

                    item represents one expense record.
                -->
                {% for item in expenses %}

                    <tr>

                        <!-- Displays the expense title. -->
                        <td>{{ item.title }}</td>

                        <!-- Displays the expense category. -->
                        <td>
                            <span class="badge">
                                {{ item.category }}
                            </span>
                        </td>

                        <!--
                            Displays the expense date.

                            strftime formats the date as:
                            Year-Month-Day.
                        -->
                        <td>
                            {{ item.created_at.strftime('%Y-%m-%d') }}
                        </td>

                        <!-- Displays the expense amount. -->
                        <td class="amount">
                            ${{ "%.2f"|format(item.amount) }}
                        </td>

                        <!-- Delete button section. -->
                        <td>

                            <!--
                                Sends a POST request to the delete route.

                                url_for generates the URL using:
                                delete_expense = Flask function name.
                                expense_id = ID of the selected expense.
                            -->
                            <form method="POST"
                                  action="{{ url_for('delete_expense', expense_id=item.id) }}">

                                <button type="submit" class="btn delete-btn">
                                    Delete
                                </button>

                            </form>

                        </td>

                    </tr>

                <!--
                    Executes when there are no expenses
                    in the expenses list.
                -->
                {% else %}

                    <tr>

                        <!-- colspan="5" combines five table columns. -->
                        <td colspan="5" class="empty-state">
                            No expenses logged yet.
                        </td>

                    </tr>

                <!-- Ends the expenses loop. -->
                {% endfor %}

            </tbody>

        </table>

    </section>

    </div>


    <!-- -------------------------------------------------
         7. EXPENSE DISTRIBUTION PIE CHART
    -------------------------------------------------- -->

    <h2>Expense Distribution</h2>

    <!--
        Checks whether Python successfully generated the pie chart.

        chart_created is a Boolean variable:
        True = Chart was created.
        False = Chart was not created.
    -->
    {% if chart_created %}

        <!--
            Displays the generated pie chart.

            url_for locates piechart.png inside the static folder.
            alt provides alternative text for the image.
            width sets the image width to 400 pixels.
        -->
        <img
            src="{{ url_for('static', filename='piechart.png') }}"
            alt="Expense Pie Chart"
            width="400"
        >

    <!-- Executes when chart_created is False. -->
    {% else %}

        <p>No expenses available yet.</p>

    <!-- Ends the conditional statement. -->
    {% endif %}


</body>

</html>


<!-- -------------------------------------------------
     8. ADDITIONAL EXPENSE DISPLAY
-------------------------------------------------- -->

<!--
    Checks whether the expenses list contains records.
-->
{% if expenses %}

    <!-- Loops through all expense records. -->
    {% for expense in expenses %}

        <!-- Displays each expense title. -->
        <p>{{ expense.title }}</p>

    <!-- Ends the loop. -->
    {% endfor %}

<!-- Executes if no expenses exist. -->
{% else %}

    <p>No expenses logged yet.</p>

<!-- Ends the conditional statement. -->
{% endif %}

--------------------------------------------------------------------------------------------------------
app.py 

# ---------------------------------------------------------
# 1. IMPORTING LIBRARIES
# ---------------------------------------------------------

# Flask: Creates and manages the web application.
# render_template: Displays HTML files from the templates folder.
# request: Retrieves information submitted through HTML forms.
# redirect: Redirects the user to another route.
# url_for: Generates URLs using function names.

from flask import Flask, render_template, request, redirect, url_for

# SQLAlchemy: Allows Python to communicate with the database.
from flask_sqlalchemy import SQLAlchemy

# datetime: Handles dates and times.
# timezone: Allows us to work with timezone-aware dates and times.
from datetime import datetime, timezone


# Matplotlib is used to generate graphs and charts.
import matplotlib

# Agg is a non-interactive backend.
# It allows Matplotlib to generate images without opening a window.
matplotlib.use("Agg")

import matplotlib.pyplot as plt


# ---------------------------------------------------------
# 2. FLASK APPLICATION CONFIGURATION
# ---------------------------------------------------------

# Creates the Flask application.
app = Flask(__name__)

# Specifies the location and name of the SQLite database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'

# Disables unnecessary modification notifications.
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

# Connects SQLAlchemy to our Flask application.
db = SQLAlchemy(app)


# ---------------------------------------------------------
# 3. DATABASE MODEL
# ---------------------------------------------------------

# A database model defines the structure of a database table.
# Here, the Expense class represents the expenses table.

class Expense(db.Model):

    # Unique ID for every expense.
    # primary_key=True means each expense has its own identifier.
    id = db.Column(db.Integer, primary_key=True)

    # Stores the expense name.
    # String(100) allows up to 100 characters.
    # nullable=False means this field cannot be empty.
    title = db.Column(db.String(100), nullable=False)

    # Stores the expense amount as a decimal number.
    amount = db.Column(db.Float, nullable=False)

    # Stores the expense category.
    category = db.Column(db.String(50), nullable=False)

    # Automatically records when an expense is created.
    # datetime.now(timezone.utc) provides the current UTC time.
    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc)
    )


# ---------------------------------------------------------
# 4. CREATING THE PIE CHART
# ---------------------------------------------------------

def create_pie_chart():

    # Retrieves expense categories and calculates
    # the total amount spent in each category.
    #
    # GROUP BY groups expenses with the same category.
    # SUM calculates the total amount for each category.

    results = db.session.query(
        Expense.category,
        db.func.sum(Expense.amount)
    ).group_by(Expense.category).all()

    # If there are no expenses, no chart can be created.
    if not results:
        return False

    # Extracts category names from the database results.
    categories = [row[0] for row in results]

    # Extracts the total spending for each category.
    amounts = [float(row[1]) for row in results]

    # Creates a figure with a width and height of 6 inches.
    plt.figure(figsize=(6, 6))

    # Generates the pie chart.
    # labels displays category names.
    # autopct displays percentage values.
    plt.pie(
        amounts,
        labels=categories,
        autopct="%1.1f%%"
    )

    # Adds a title to the chart.
    plt.title("Expenses by Category")

    # Saves the chart as an image inside the static folder.
    plt.savefig("static/piechart.png")

    # Closes the figure to free up memory.
    plt.close()

    # Returns True if the chart was successfully generated.
    return True


# ---------------------------------------------------------
# 5. MAIN ROUTE (HOME PAGE)
# ---------------------------------------------------------

# The '/' represents the homepage.
# GET: Requests information from the server.
# POST: Sends information to the server.

@app.route('/', methods=['GET', 'POST'])
def index():

    # Checks whether the user submitted the HTML form.
    if request.method == "POST":

        # Retrieves the expense title from the HTML form.
        # strip() removes unnecessary spaces.
        title = request.form.get('title', '').strip()

        # Retrieves the expense amount.
        amount_raw = request.form.get('amount', '0')

        # Retrieves the category.
        # Uses General if no category is provided.
        category = request.form.get('category', 'General')

        # Checks whether the title and amount are provided.
        if title and amount_raw:

            try:
                # Creates a new Expense object.
                new_expense = Expense(
                    title=title,
                    amount=float(amount_raw),
                    category=category
                )

                # Adds the new expense to the database session.
                db.session.add(new_expense)

                # Saves the changes permanently in the database.
                db.session.commit()

            # Handles invalid numeric values.
            except ValueError:
                pass

        # Redirects the user to the homepage.
        # This prevents accidental form resubmission on refresh.
        return redirect(url_for('index'))

    # -----------------------------------------------------
    # 6. FETCHING EXPENSES AND CALCULATING TOTAL SPENDING
    # -----------------------------------------------------

    # Retrieves all expenses.
    # order_by sorts them from newest to oldest.
    expenses = Expense.query.order_by(
        Expense.created_at.desc()
    ).all()

    # Calculates the total amount spent.
    total_spent = sum(item.amount for item in expenses)

    # -----------------------------------------------------
    # 7. CATEGORY-WISE EXPENSE CALCULATION
    # -----------------------------------------------------

    # Creates an empty dictionary.
    # It will store each category and its total spending.
    category_totals = {}

    # Goes through every expense in the database.
    for item in expenses:

        # Adds the expense amount to its category total.
        #
        # get() retrieves the existing total.
        # If the category does not exist, it starts at 0.0.
        category_totals[item.category] = (
            category_totals.get(item.category, 0.0)
            + item.amount
        )

    # Generates the pie chart.
    chart_created = create_pie_chart()

    # -----------------------------------------------------
    # 8. SENDING DATA TO THE HTML PAGE
    # -----------------------------------------------------

    # render_template opens index.html.
    #
    # The variables below become available inside the HTML
    # template through the Jinja2 template engine.

    return render_template(
        'index.html',
        expenses=expenses,
        total_spent=total_spent,
        category_totals=category_totals,
        chart_created=chart_created
    )


# ---------------------------------------------------------
# 9. DELETING AN EXPENSE
# ---------------------------------------------------------

# Creates a route for deleting a particular expense.
# <int:expense_id> captures an integer from the URL.
# POST ensures deletion is requested through a form submission.

@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):

    # Searches the database for the expense using its ID.
    expense = db.session.get(Expense, expense_id)

    # Checks whether the expense exists.
    if expense:

        # Removes the expense from the database session.
        db.session.delete(expense)

        # Permanently saves the deletion.
        db.session.commit()

    # Redirects the user to the homepage.
    return redirect(url_for('index'))


# ---------------------------------------------------------
# 10. CREATING THE DATABASE
# ---------------------------------------------------------

# Creates an application context.
# This allows Flask-specific operations to work outside routes.

with app.app_context():

    # Creates the database tables if they do not already exist.
    db.create_all()


# ---------------------------------------------------------
# 11. RUNNING THE APPLICATION
# ---------------------------------------------------------

# Checks whether this file is being executed directly.
if __name__ == '__main__':

    # Starts the Flask development server.
    # debug=True automatically reloads the application
    # when code changes and displays debugging information.
    app.run(debug=True)

--------------------------------------------------------------------------------------------------------
test_app.py

# --------------------------------------------------
# 1. IMPORTING LIBRARIES AND APPLICATION COMPONENTS
# --------------------------------------------------

# pytest is a Python testing framework.
# It helps us write and execute automated tests.
import pytest

# Imports the Flask application, database and Expense model
# from our main app.py file.
from app import app, db, Expense


# --------------------------------------------------
# 2. FIXTURE: PREPARING THE TESTING ENVIRONMENT
# --------------------------------------------------

# @pytest.fixture creates a fixture.
# A fixture prepares resources that can be reused by multiple tests.
@pytest.fixture
def client():

    # Updates the Flask configuration for testing.
    app.config.update(

        # Enables testing mode.
        TESTING=True,

        # Creates an in-memory SQLite database.
        # This database exists temporarily during testing.
        SQLALCHEMY_DATABASE_URI='sqlite:///:memory:',

        # Disables CSRF protection for testing.
        WTF_CSRF_ENABLED=False
    )

    # Creates an application context.
    # This allows database operations outside Flask routes.
    with app.app_context():

        # Creates the database tables for testing.
        db.create_all()

        # Creates a test client.
        # It simulates browser requests without opening a real browser.
        with app.test_client() as test_client:

            # Provides the test client to individual test functions.
            yield test_client

        # Removes the current database session after testing.
        db.session.remove()

        # Deletes the temporary database tables.
        db.drop_all()


# --------------------------------------------------
# 3. GET / (INDEX PAGE) TESTS
# --------------------------------------------------

# Tests whether the homepage works when there are no expenses.
def test_index_empty_state(client):

    # Sends a GET request to the homepage.
    response = client.get('/')

    # Checks whether the server responds successfully.
    # HTTP status code 200 means OK.
    assert response.status_code == 200

    # Converts the response content from bytes into a string.
    html = response.data.decode('utf-8')

    # Checks whether the homepage contains the correct heading.
    assert "Expense Tracker" in html

    # Checks whether the empty-state message is displayed.
    assert "No expenses logged yet." in html

    # Checks whether the total expenditure starts at zero.
    assert "$0.00" in html


# Tests whether existing expenses appear on the homepage.
def test_index_with_existing_data(client):

    # Creates an application context for database operations.
    with app.app_context():

        # Creates a sample expense.
        item = Expense(
            title="Lunch",
            amount=12.50,
            category="Food & Dining"
        )

        # Adds the sample expense to the database session.
        db.session.add(item)

        # Saves the expense in the database.
        db.session.commit()

    # Requests the homepage.
    response = client.get('/')

    # Checks whether the request was successful.
    assert response.status_code == 200

    # Converts the response into readable HTML text.
    html = response.data.decode('utf-8')

    # Checks whether the expense information is displayed.
    assert "Lunch" in html
    assert "$12.50" in html
    assert "Food & Dining" in html


# --------------------------------------------------
# 4. POST / (CREATE EXPENSE) TESTS
# --------------------------------------------------

# Tests whether a valid expense can be created successfully.
def test_create_expense_valid(client):

    # Creates sample form data.
    payload = {
        'title': 'Bus Pass',
        'amount': '45.00',
        'category': 'Transportation'
    }

    # Sends a POST request containing the expense information.
    # follow_redirects=True follows the redirect to the homepage.
    response = client.post('/', data=payload, follow_redirects=True)

    # Checks whether the final response is successful.
    assert response.status_code == 200

    # Checks whether the expense was saved in the database.
    with app.app_context():

        # Searches for an expense with the title 'Bus Pass'.
        expense = Expense.query.filter_by(title='Bus Pass').first()

        # Checks that the expense exists.
        assert expense is not None

        # Checks whether the saved amount is correct.
        assert expense.amount == 45.00

        # Checks whether the saved category is correct.
        assert expense.category == 'Transportation'

    # Checks whether the newly created expense appears on the webpage.
    html = response.data.decode('utf-8')

    assert "Bus Pass" in html
    assert "$45.00" in html


# Tests whether the application rejects an invalid amount.
def test_create_expense_invalid_amount(client):

    # Creates form data with an invalid numerical value.
    payload = {
        'title': 'Broken Data',
        'amount': 'invalid_number',
        'category': 'General'
    }

    # Submits the invalid expense information.
    response = client.post('/', data=payload, follow_redirects=True)

    # Checks whether the application redirects successfully.
    assert response.status_code == 200

    # Checks whether the invalid expense was prevented from being saved.
    with app.app_context():

        # Counts the number of expenses in the database.
        count = Expense.query.count()

        # Confirms that no expense was saved.
        assert count == 0


# Tests whether an expense with an empty title is rejected.
def test_create_expense_empty_title(client):

    # Creates form data containing only blank spaces as the title.
    payload = {
        'title': '   ',
        'amount': '25.00',
        'category': 'Utilities'
    }

    # Submits the form.
    response = client.post('/', data=payload, follow_redirects=True)

    # Checks whether the response is successful.
    assert response.status_code == 200

    # Checks whether the empty-title expense was saved.
    with app.app_context():

        # Counts the saved expenses.
        count = Expense.query.count()

        # Confirms that no expense was created.
        assert count == 0


# --------------------------------------------------
# 5. EXPENSE CALCULATOR AND AGGREGATION TESTS
# --------------------------------------------------

# Tests whether total expenditure and category breakdowns
# are calculated correctly.
def test_expense_totals_and_breakdowns(client):

    # Creates an application context for database operations.
    with app.app_context():

        # Creates the first sample expense.
        e1 = Expense(
            title="Dinner",
            amount=30.00,
            category="Food & Dining"
        )

        # Creates the second sample expense.
        e2 = Expense(
            title="Coffee",
            amount=5.50,
            category="Food & Dining"
        )

        # Creates the third sample expense.
        e3 = Expense(
            title="Internet",
            amount=60.00,
            category="Utilities"
        )

        # Adds all three expenses to the database session.
        db.session.add_all([e1, e2, e3])

        # Saves all three expenses.
        db.session.commit()

    # Requests the homepage to retrieve calculated results.
    response = client.get('/')

    # Converts the webpage response into readable text.
    html = response.data.decode('utf-8')

    # Checks whether the total expenditure is correct.
    # 30.00 + 5.50 + 60.00 = 95.50
    assert "$95.50" in html

    # Checks the Food & Dining category total.
    # 30.00 + 5.50 = 35.50
    assert "$35.50" in html

    # Checks the Utilities category total.
    assert "$60.00" in html


# --------------------------------------------------
# 6. POST /delete/<id> TESTS
# --------------------------------------------------

# Tests whether an existing expense can be deleted.
def test_delete_expense_success(client):

    # Creates an application context.
    with app.app_context():

        # Creates a sample expense to delete.
        item = Expense(
            title="Snack",
            amount=3.00,
            category="Food & Dining"
        )

        # Adds the expense to the database.
        db.session.add(item)

        # Saves the expense.
        db.session.commit()

        # Stores the expense ID before deletion.
        item_id = item.id

    # Sends a POST request to the delete route.
    # The URL contains the ID of the expense to delete.
    response = client.post(
        f'/delete/{item_id}',
        follow_redirects=True
    )

    # Checks whether the deletion request was successful.
    assert response.status_code == 200

    # Checks whether the expense was removed from the database.
    with app.app_context():

        # Searches for the deleted expense using its ID.
        deleted = db.session.get(Expense, item_id)

        # None means the expense no longer exists.
        assert deleted is None


# Tests how the application handles a non-existent expense ID.
def test_delete_non_existent_expense(client):

    # Attempts to delete an expense with ID 9999.
    # This ID does not exist in the test database.
    response = client.post(
        '/delete/9999',
        follow_redirects=True
    )

    # Checks whether the application handles the request
    # without producing a server error.
    assert response.status_code == 200

--------------------------------------------------------------------------------------------------------
folder structure of expense tracker project:

Expense Tracker/
│
├── app.py
├── README.md
├── requirements.txt
├── expenses.db
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── piechart.png
│
└── tests/
    └── test_app.py