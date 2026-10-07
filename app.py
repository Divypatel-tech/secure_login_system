from flask import Flask, render_template, request, redirect, session, url_for
import bcrypt
from database import init_db, get_db

app = Flask(__name__)
app.secret_key = 'your_secret_key_change_this'  # Change this to anything random

# Initialize database when app starts
init_db()

# ---------- REGISTER ----------
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username'].strip()
        email    = request.form['email'].strip()
        password = request.form['password'].strip()

        # Basic validation
        if not username or not email or not password:
            error = 'All fields are required.'
        elif len(password) < 6:
            error = 'Password must be at least 6 characters.'
        else:
            # Hash password
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            try:
                db = get_db()
                db.execute(
                    'INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
                    (username, email, password_hash)
                )
                db.commit()
                db.close()
                return redirect(url_for('login'))
            except Exception:
                error = 'Username or email already exists.'

    return render_template('register.html', error=error)


# ---------- LOGIN ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        if not username or not password:
            error = 'All fields are required.'
        else:
            db = get_db()
            user = db.execute(
                'SELECT * FROM users WHERE username = ?', (username,)
            ).fetchone()
            db.close()

            if user and bcrypt.checkpw(password.encode('utf-8'), user['password_hash']):
                session['user'] = username
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid username or password.'

    return render_template('login.html', error=error)


# ---------- DASHBOARD (Protected) ----------
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['user'])


# ---------- LOGOUT ----------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# ---------- HOME ----------
@app.route('/')
def home():
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)