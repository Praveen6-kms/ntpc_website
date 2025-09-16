from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
from datetime import datetime
from werkzeug.utils import secure_filename
from datetime import date

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def init_db():
    conn = sqlite3.connect("updates.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS updates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            message TEXT,
            start_date TEXT,
            end_date TEXT,
            image TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin123':
            session['logged_in'] = True
            flash('Login successful.', 'success')
            return redirect(url_for('add_news'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('admin_login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('admin_login'))

@app.route('/add-news', methods=['GET', 'POST'])
def add_news():
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))

    if request.method == 'POST':
        title = request.form['title']
        message = request.form['message']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        image_file = request.files.get('image')
        image_filename = ""

        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(image_path)
            image_filename = filename

        conn = sqlite3.connect("updates.db")
        c = conn.cursor()
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("INSERT INTO updates (title, message, start_date, end_date, image, created_at) VALUES (?, ?, ?, ?, ?, ?)",
          (title, message, start_date, end_date, image_filename, created_at))
        conn.commit()
        conn.close()
        flash('Update added successfully.', 'success')
        return redirect(url_for('add_news'))

    return render_template('add_news.html')

@app.route('/manage-updates')
def manage_updates():
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))

    conn = sqlite3.connect("updates.db")
    c = conn.cursor()
    c.execute("SELECT * FROM updates ORDER BY id DESC")
    updates = c.fetchall()
    conn.close()
    return render_template('manage_updates.html', updates=updates)

@app.route('/edit-update/<int:update_id>', methods=['GET', 'POST'])
def edit_update(update_id):
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))

    conn = sqlite3.connect("updates.db")
    c = conn.cursor()

    if request.method == 'POST':
        title = request.form['title']
        message = request.form['message']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        image_file = request.files.get('image')
        image_filename = request.form.get('old_image', '')

        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(image_path)
            image_filename = filename

        c.execute("UPDATE updates SET title=?, message=?, start_date=?, end_date=?, image=? WHERE id=?",
                  (title, message, start_date, end_date, image_filename, update_id))
        conn.commit()
        conn.close()
        flash('Update modified successfully.', 'info')
        return redirect(url_for('manage_updates'))

    c.execute("SELECT * FROM updates WHERE id=?", (update_id,))
    update = c.fetchone()
    conn.close()
    return render_template('edit_update.html', update=update)

@app.route('/delete-update/<int:update_id>')
def delete_update(update_id):
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))

    conn = sqlite3.connect("updates.db")
    c = conn.cursor()
    c.execute("DELETE FROM updates WHERE id=?", (update_id,))
    conn.commit()
    conn.close()
    flash('Update deleted.', 'warning')
    return redirect(url_for('manage_updates'))

@app.route('/')
def home():
    today = date.today().isoformat()
    conn = sqlite3.connect("updates.db")
    c = conn.cursor()
    c.execute("SELECT id, title, message, start_date, end_date, image, created_at FROM updates WHERE end_date >= ? ORDER BY id DESC", (today,))

    updates = c.fetchall()
    conn.close()
    return render_template('frontend.html', updates=updates)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




