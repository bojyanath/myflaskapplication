import os
from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app=Flask(__name__,template_folder='templates')

# Initialize MySQL
#mysql = MySQL(app)
#initialize postgres connection
conn = psycopg2.connect(database="achievers",
                        user=os.environ.get("DB_USER"),
                        password=os.environ.get("DB_USER_PWD"),
                        host=os.environ.get("DB_HOST"),
                        port="5432")
@app.route('/')
def hello():
    cur = conn.cursor()
    cur.execute('SELECT message FROM dbo.messages')
    messages = cur.fetchall()#messages is varaible
    cur.close()
    return render_template('index.html' ,messages=messages) #msgs is A varaible in UI

@app.route('/submit', methods=['POST'])
def submit():
    new_message = request.form.get('new_message')
    cur = conn.cursor()
    cur.execute('INSERT INTO dbo.messages (message) VALUES (%s)', [new_message])
    conn.commit()
    cur.close()
    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

