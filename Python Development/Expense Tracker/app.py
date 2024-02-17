from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL, category TEXT, date TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Route for home page
@app.route('/')
def home():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT * FROM expenses ORDER BY date DESC")
    expenses = c.fetchall()
    conn.close()
    return render_template('index.html', expenses=expenses)

# Route for adding expenses
@app.route('/add', methods=['POST'])
def add_expense():
    amount = float(request.form['amount'])
    category = request.form['category']
    date = request.form['date']
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)", (amount, category, date))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

# Route for viewing spending patterns
@app.route('/patterns')
def patterns():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT date, SUM(amount) FROM expenses GROUP BY date ORDER BY date")
    data = c.fetchall()
    conn.close()

    dates = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, amounts, marker='o')
    plt.title('Spending Patterns Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Amount Spent')
    plt.xticks(rotation=45)
    
    # Convert plot to base64 for displaying in HTML
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('patterns.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
