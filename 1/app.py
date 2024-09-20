from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to insert user data into the database
def save_user_to_db(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Insert the username and password into the users table
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        return "Username already exists. Please try another username."
    finally:
        conn.close()

    return "User registered successfully."

# Route for the registration form (login.html)
@app.route('/')
def home():
    return render_template('login.html')

# Route to handle form submission
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    # Save user to the database
    message = save_user_to_db(username, password)
    
    return message

if __name__ == '__main__':
    app.run(debug=True)
