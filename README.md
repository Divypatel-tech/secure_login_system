[README.md](https://github.com/user-attachments/files/33138396/README.md)
# 🔐 Secure Login System

A secure web application built with **Python Flask** that demonstrates real-world authentication best practices — including hashed passwords, session management, SQL injection prevention, and input validation.

> ⚠️ **Educational Project** — Built as part of a cybersecurity internship to demonstrate secure authentication concepts.
h
## ✨ Features

- ✅ **User Registration** — with input validation and duplicate detection
- ✅ **Secure Password Hashing** — using `bcrypt` (never stored in plain text)
- ✅ **User Login** — with session-based authentication
- ✅ **Protected Routes** — dashboard accessible only when logged in
- ✅ **Logout** — clears session securely
- ✅ **SQL Injection Prevention** — parameterized queries throughout
- ✅ **Input Validation** — empty fields, minimum password length

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| Database | SQLite3 |
| Password Hashing | bcrypt |
| Frontend | HTML5, CSS3 (Jinja2 Templates) |
| Sessions | Flask built-in sessions |

---

## 📁 Project Structure

```
secure_login/
│
├── app.py              # Main Flask application & routes
├── database.py         # Database initialization & connection
├── users.db            # SQLite database (auto-created on first run)
│
└── templates/
    ├── register.html   # Registration page
    ├── login.html      # Login page
    └── dashboard.html  # Protected dashboard page
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/secure-login-system.git
cd secure-login-system
```

### 2. Install Required Libraries

```bash
pip install flask bcrypt
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open in Browser

```
http://127.0.0.1:5000
```

---

## 🔒 Security Concepts Demonstrated

### 🔑 Password Hashing (bcrypt)
Passwords are never stored in plain text. bcrypt adds a salt and hashes the password before storing it in the database.

```python
# Hashing on register
password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Verifying on login
bcrypt.checkpw(password.encode('utf-8'), user['password_hash'])
```

### 🛡️ SQL Injection Prevention
All database queries use parameterized inputs — never string concatenation.

```python
# ✅ Safe — parameterized query
db.execute('SELECT * FROM users WHERE username = ?', (username,))

# ❌ Dangerous — never do this
query = "SELECT * FROM users WHERE username = '" + username + "'"
```

### 🔐 Session Management
Flask sessions are used to track logged-in users. Protected routes redirect unauthenticated users back to login.

```python
# Set session on login
session['user'] = username

# Protect routes
if 'user' not in session:
    return redirect(url_for('login'))

# Clear on logout
session.clear()
```

---

## 🚀 How to Use

1. Go to `http://127.0.0.1:5000/register`
2. Create an account with a username, email, and password
3. You'll be redirected to the login page
4. Log in with your credentials
5. You'll land on the protected dashboard
6. Click **Logout** to end your session

---

## 📋 Requirements

```
Python 3.7+
Flask
bcrypt
```

Or install via:
```bash
pip install flask bcrypt
```

---

## 🗺️ Future Improvements

- [ ] Two-Factor Authentication (2FA) using `pyotp`
- [ ] Email verification on registration
- [ ] Password reset via email
- [ ] Rate limiting to prevent brute-force attacks
- [ ] CSRF token protection
- [ ] Remember Me functionality

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/YOUR_PROFILE)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- Built as **Task 4** of the **Thiranex CS Cybersecurity Internship**
- Inspired by real-world secure authentication systems
- Flask documentation: https://flask.palletsprojects.com
